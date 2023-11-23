from django.urls import path, include
from . import views


app_name = "home"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.HomeView.as_view(), name='home'),
    path('<int:pk>/equipments/', include('equipment.urls'))
]