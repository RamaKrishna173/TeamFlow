from django.urls import path
from . import views

urlpatterns = [
    path("", views.calendar, name="calendar"),
    path("events/", views.events, name="calendar_events"),
    path("update/", views.update_event, name="update_event"),
]