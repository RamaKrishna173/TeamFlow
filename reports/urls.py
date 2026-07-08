from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_home, name='reports_home'),
    path('projects/', views.export_projects, name='export_projects'),
    path('tasks/', views.export_tasks, name='export_tasks'),
]