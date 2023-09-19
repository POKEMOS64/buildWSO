from django.urls import path

from .views import questViews

app_name = 'question'

urlpatterns = [
    path('', questViews, name='question')
]
