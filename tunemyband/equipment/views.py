from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Equipment


def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, "equipment/show_equipments.html", {'equipments': equipments})


def equipment_by_owner(request, owner):
    equipments = get_object_or_404(Equipment, owner=owner)
    return render(request, 'equipment/show_equipment_by_owner.html', {'equipments': equipments})
