from django.shortcuts import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Equipment


def user_equipments(request, username):
    equipments = Equipment.objects.filter(owner__username=username)
    return HttpResponse(request,  {'equipments': equipments})


def music_band_equipments(request, username, music_band):
    equipments = Equipment.objects.filter(owner__username=username, music_band=music_band)
    return HttpResponse(request,  {'equipments': equipments})
