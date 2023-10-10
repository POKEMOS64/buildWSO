from django.urls import path

from .views import Kvit

app_name='kvit'

urlpatterns=[
    path('index/', Kvit , name='index'),
]