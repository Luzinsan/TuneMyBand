from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def home(request):
    return render(request, 'home/home.html', {})


def sign_in(request):
    return render(request, 'home/sign_in.html', {})


def sign_up(request):
    return render(request, 'home/sign_up.html', {})


