from django.urls import path

from .views import AbonViews, AbonIndication, AbonZamenaPu,AbonDisruption


app_name = 'Abon'

urlpatterns = [
    path('', AbonViews, name='abon'),
    path('abonentskiy/abonzamenapu/', AbonZamenaPu, name='abonzamenapu'),
    path('abonentskiy/abondisruption/', AbonDisruption, name='abondisruption'),
    path('indication/', AbonIndication, name='indication'),

]
