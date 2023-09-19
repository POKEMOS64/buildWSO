from django.urls import path

from ls.views import LsModelView, inducaions

app_name = 'ls'

urlpatterns = [
    path('', LsModelView, name='ls'),
    path('inducations/', inducaions, name='inducations'),
]
