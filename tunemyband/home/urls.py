from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.UserProfileCreateView.as_view(), name='sign_up'),
]
