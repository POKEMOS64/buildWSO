from django.urls import path

from ls.views import LsModelView, inducaions,ResultViews

app_name = 'ls'

urlpatterns = [
    path('', LsModelView, name='ls'),
    path('finish',ResultViews,name='result'),
    path('inducations/', inducaions, name='inducations'),
]
