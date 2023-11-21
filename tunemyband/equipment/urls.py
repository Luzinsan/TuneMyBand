from django.urls import path
from . import views


urlpatterns = [
    path("", views.user_equipments, name='user_equipments'),
    path("<str:music_band>/", views.music_band_equipments, name='music_band_equipments'),
]
