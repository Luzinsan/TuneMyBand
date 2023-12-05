from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('favicon.ico/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('band/', include('band.urls')),
    # path('bands/', views.BandsView.as_view(), name='bands'),
    # path('users/', views.UsersView.as_view(), name='users'),
    # path('', views.IndexView.as_view(), name='index'),
]
