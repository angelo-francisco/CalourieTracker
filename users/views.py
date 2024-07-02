from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def _signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "users/signup.html", {"form": form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
        # TODO: Implementar mensagens de erro
        return redirect(reverse("signup"))


def _login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tracker_auth"))
        # TODO: Implementar mensagens de erro
        return redirect(reverse("login"))


def _logout(request): ...
