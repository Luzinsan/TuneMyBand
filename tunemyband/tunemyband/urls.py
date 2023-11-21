from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('favicon.ico/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('band/', include('band.urls')),
    path('', include('app_auth.urls')),
]
