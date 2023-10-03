from django.urls import path

from .views import Informations, WaterSupply, WaterDis,CNNpages,show_post

app_name = 'informations'

urlpatterns = [
    path('', Informations, name='info'),
    path('water/', WaterSupply, name='watersupply'),
    path('disposal/', WaterDis, name='waterdis'),
    path('post/', CNNpages, name='infocnn'),
    path('post/<int:post_id>/',show_post,name='post')
]
