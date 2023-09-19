from django.urls import path

from advertisement.views import AdvertView

app_name = 'advertisement'

urlpatterns = [
    path('', AdvertView, name='advertisement')
]
