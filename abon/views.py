from django.shortcuts import render

# Create your views here.


def AbonViews(request):
    return render(request, 'abon/abon_pages.html')


def AbonIndication(request):
    return render(request, 'abon/indication_pages.html')
