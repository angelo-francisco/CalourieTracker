from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required(login_url=reverse("login"))
def trackerAuth(request):
    return render(request, "tracker/auth.html")
