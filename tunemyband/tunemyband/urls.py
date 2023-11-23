from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('favicon.ico/', admin.site.urls),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('band/', include('band.urls')),
    path('', include('home.urls')),
]
