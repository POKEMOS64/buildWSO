from django.shortcuts import render
from informations.models import indxpages
# Create your views here.


def AbonViews(request):
    index__ = indxpages.objects.all().filter(pk=4)
    return render(request, 'abon/abon_pages.html', {'index': index__})

def AbonZamenaPu(request):
    index__ = indxpages.objects.all().filter(pk=5)
    return render(request, 'abon/abon_pages_zamena_pu.html', {'index': index__})


def AbonIndication(request):
    return render(request, 'abon/indication_pages.html')
