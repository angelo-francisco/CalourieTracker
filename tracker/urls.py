from django.urls import path
from . import views

urlpatterns = [path("auth/", views.trackerAuth, "tracker_auth")]
