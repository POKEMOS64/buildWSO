from django.urls import path

from .views import Informations, WaterSupply, WaterDis

app_name = 'informations'

urlpatterns = [
    path('', Informations, name='info'),
    path('water/', WaterSupply, name='watersupply'),
    path('disposal/', WaterDis, name='waterdis')
]
