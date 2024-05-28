from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path("konto/", include("django.contrib.auth.urls")),
    path("rejestracja/", views.registration_view, name="rejestracja"),
]