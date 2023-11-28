from django.urls import path, include
from . import views

app_name = 'band'
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('equipments/', include('equipment.urls'))

]
