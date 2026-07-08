from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile



def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        if not username or not password:

            messages.error(
                request,
                "Please enter username and password"
            )

            return redirect('login')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )


            UserProfile.objects.get_or_create(
                user=user
            )


            return redirect('/')


        else:

            messages.error(
                request,
                "Invalid username or password"
            )


    return render(
        request,
        'accounts/login.html'
    )




def logout_view(request):

    logout(request)

    return redirect('/accounts/login/')





def register_view(request):

    if request.method == "POST":


        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')



        if not username or not email or not password or not confirm_password:

            messages.error(
                request,
                "Please enter full details"
            )

            return redirect('register')



        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect('register')



        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect('register')



        user = User.objects.create_user(

            username=username,

            email=email,

            password=password

        )


        UserProfile.objects.get_or_create(
            user=user
        )


        messages.success(
            request,
            "Registration successful. Please login."
        )


        return redirect('login')



    return render(
        request,
        'accounts/register.html'
    )






@login_required
def profile(request):

    user = request.user


    profile, created = UserProfile.objects.get_or_create(
        user=user
    )


    if request.method == "POST":


        username = request.POST.get('username')

        email = request.POST.get('email')

        theme = request.POST.get('theme')



        if not username or not email:

            messages.error(
                request,
                "Please enter full details"
            )

            return redirect('profile')



        user.username = username

        user.email = email

        user.save()



        if theme:

            profile.theme = theme

            profile.save()



        messages.success(
            request,
            "Profile updated successfully"
        )


        return redirect('profile')



    return render(
        request,
        'accounts/profile.html',
        {
            'user': user,
            'profile': profile
        }
    )