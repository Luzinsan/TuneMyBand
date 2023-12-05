from django.shortcuts import get_object_or_404, render
from .models import MusicBand
from django.contrib.auth.models import User
from django.views import generic
from equipment.models import Equipment
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailView(generic.DetailView):
    model = MusicBand
    template_name = "band/index.html"


def index(request):
    return render(request, "band/home.html")


class BandEquipmentList(LoginRequiredMixin, generic.ListView):
    model = Equipment
    template_name = "equipment/user_equipments.html"

    def get_queryset(self):
        # if Profile.pbjects.get(self.request.user)
        return Equipment.objects.filter(owner=self.request.user)
