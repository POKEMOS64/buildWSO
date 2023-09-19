from django.urls import path

from .views import AbonViews, AbonIndication


app_name = 'Abon'

urlpatterns = [
    path('', AbonViews, name='abon'),
    path('indication/', AbonIndication, name='indication'),

]
