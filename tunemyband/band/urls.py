from django.urls import path, include
from . import views


urlpatterns = [
    path('<str:band_name>/', views.band_home, name='band_home'),
    # path('equipments/', include('equipment.urls'))

]
