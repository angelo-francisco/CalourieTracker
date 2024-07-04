from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def _signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "users/signup.html", {"form": form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)

        if User.objects.filter(username=form.data["username"]).exists():
            messages.add_message(request, messages.WARNING, "Username já existe !")
            return redirect(reverse("signup"))

        if form.data["password1"] != form.data["password2"]:
            messages.add_message(request, messages.WARNING, "As senhas não coincidem!")
            return redirect(reverse("signup"))

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Dados cadastrados!")
            return redirect(reverse("login"))


def _login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse("tracker_auth"))
        else:
            if not User.objects.filter(username=form.data["username"]).exists():
                messages.add_message(request, messages.WARNING, "Username não existe!")
                return redirect(reverse("login"))
            messages.add_message(
                request, messages.WARNING, "Username ou senha inválidos!"
            )
            return redirect(reverse("login"))


def _logout(request):
    logout(request)
    return redirect(reverse('login'))