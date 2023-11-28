from django.views import generic

from band.models import MusicBand
from .models import Profile


class IndexView(generic.ListView):
    template_name = "home/index.html"
    context_object_name = "latest_band_list"

    def get_queryset(self):
        return MusicBand.objects.order_by('-date_created')[:5]


class HomeView(generic.DetailView):
    model = Profile
    template_name = "home/home.html"




