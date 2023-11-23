from django.urls import path
from . import views
app_name = 'equipment'

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:music_band>/", views.music_band_equipments, name='music_band_equipments'),
]
