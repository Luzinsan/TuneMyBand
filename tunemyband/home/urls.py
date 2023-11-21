from django.urls import path, include
from . import views


urlpatterns = [
    path('<str:username>', views.home, name='home'),
    path('<str:username>/equipments/', include('equipment.urls'))

]
