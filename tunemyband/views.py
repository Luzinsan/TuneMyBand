from django.views import generic

from band.models import MusicBand
from accounts.models import User


class IndexView(generic.ListView):
    template_name = "tunemyband/index.html"
    context_object_name = "latest_band_list"
    queryset = MusicBand.objects.order_by('-register_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_user_list'] = User.objects.order_by('-user__date_joined')[:5]
        return context


class BandsView(generic.ListView):
    template_name = "tunemyband/bands.html"
    model = MusicBand
    context_object_name = 'band_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BandsView, self).get_context_data(**kwargs)
        context['num_bands'] = MusicBand.objects.all().count()
        return context


class UsersView(generic.ListView):
    template_name = "tunemyband/users.html"
    model = User
    context_object_name = "user_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['num_users'] = User.objects.all().count()
        return context


