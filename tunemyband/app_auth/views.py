from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from band.models import MusicBand
from .models import CustomUser


def index(request):
    latest_registered_bands = MusicBand.objects.order_by('-date_created')[:5]
    latest_registered_users = CustomUser.objects.order_by('-date_joined')[:5]
    return render(request, 'app_auth/index.html',
                  {'bands': latest_registered_bands,
                   'users': latest_registered_users})


def sign_in(request):
    return render(request, 'app_auth/sign_in.html', {})


def sign_up(request):
    return render(request, 'app_auth/sign_up.html', {})
