from django.shortcuts import render
from .models import MusicBand
from app_auth.models import CustomUser


def band_home(request, band_name):
    band = MusicBand.objects.get(name=band_name)
    return render(request, 'band/band_home.html', {'band': band})

