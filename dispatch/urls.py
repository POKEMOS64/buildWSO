from django.urls import path

from dispatch.views import dispatchViews

app_name = 'dispatch'

urlpatterns = [
    path('', dispatchViews, name='dispat')
]
