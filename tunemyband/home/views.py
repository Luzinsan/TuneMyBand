from django.shortcuts import render
from app_auth.models import CustomUser


def home(request, username: str):
    user = CustomUser.objects.get(username=username)
    return render(request, 'home/home.html', {'user': user})


