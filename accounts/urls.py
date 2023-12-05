from django.urls import path, include
from . import views


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    # path('<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('profile/', views.home, name='home'),
    # path("equipments/", views.UserEquipmentList.as_view(), name='user_equipments'),
]