from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from bands.urls import urlpatterns as band_urls
from breaks.urls import urlpatterns as breaks_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += band_urls
urlpatterns += breaks_urls
urlpatterns += user_urls
