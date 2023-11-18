from django.urls import path

from .views import Informations, WaterSupply, WaterDis,CNNpages,show_post,InfoPagesVakans,InfoPagesPolitika

app_name = 'informations'

urlpatterns = [
    path('', Informations, name='info'),
    path('privacy_policy/', InfoPagesPolitika, name='privacy'),
    path('job-openings/', InfoPagesVakans, name='job'),
    path('water/', WaterSupply, name='watersupply'),
    path('disposal/', WaterDis, name='waterdis'),
    path('post/', CNNpages, name='infocnn'),
    path('post/<int:post_id>/',show_post,name='post')
]
