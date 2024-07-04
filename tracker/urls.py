from django.urls import path
from . import views


urlpatterns = [
    path("auth/", views.trackerAuth, name="tracker_auth"),
    path("", views.tracker, name="tracker"),
    path("delete/<int:id>", views.delete_consumed_food, name="delete_consumed"),
]
