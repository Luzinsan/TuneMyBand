from django.shortcuts import render
from django.utils import timezone
from .models import Equipment


def show(request):
    equipments = Equipment.objects.all()
    return render(request, "equipment/show_equipments.html", {'equipments': equipments})

