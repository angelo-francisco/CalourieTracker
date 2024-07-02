from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views._signup, name="signup"),
    path("login/", views._login, name="login"),
]
