from django.shortcuts import get_object_or_404, render
from .models import MusicBand
from django.contrib.auth.models import User
from django.views import generic


class DetailView(generic.DetailView):
    model = MusicBand
    template_name = "band/index.html"

