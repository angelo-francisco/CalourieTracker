from django.urls import path
import os
import sys


abspath = os.path.abspath(os.curdir)
sys.path.insert(0, abspath)

from users import views

urlpatterns = [
    path("signup/", views._signup, name="signup"),
    path("login/", views._login, name="login"),
    path("logout/", views._logout, name="logout"),
]
