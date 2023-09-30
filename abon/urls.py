from django.urls import path

from .views import AbonViews, AbonIndication, AbonZamenaPu


app_name = 'Abon'

urlpatterns = [
    path('', AbonViews, name='abon'),
    path('abonentskiy/abonzamenapu/', AbonZamenaPu, name='abonzamenapu'),
    path('indication/', AbonIndication, name='indication'),

]
