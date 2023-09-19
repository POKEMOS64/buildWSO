from django.urls import path

from debt.views import debtViews

app_name = 'debt'

urlpatterns = [
    path('', debtViews, name='debt')
]
