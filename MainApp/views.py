from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from .forms import RegisterForm
from BlogApp.models import Author

def main_view(request):
    return redirect("main")

def registration_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            author = Author(user=user, nickname=user.username)
            author.save()
            login(request, user)
            return redirect("main")  # Redirect to main page after successful registration
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})