from django.shortcuts import render
from django.http import HttpResponse
from .models import WaterModel, WaterModelDoc, WaterModelDocDisposal, InfoModelDoc, InfoModelDocLast, InfoModelDocbeforeLast, InfoModelDocnazLast, indxpages
# Create your views here.


def InfoPagesIdx(request):
    index__ = indxpages.objects.all().filter(pk=1)
    return render(request, 'informations/index.html', {'index': index__})

def InfoPagesContact(request):
    index__ = indxpages.objects.all().filter(pk=2)
    return render(request, 'informations/index.html', {'index': index__})


def WaterSupply(request):
    WaterSupp = WaterModel.objects.all().filter(pk=1)
    documentTypes = WaterModelDoc.objects.all()
    return render(request, 'informations/info_index_watersupply.html', {'waterpages': WaterSupp, 'document': documentTypes})


def WaterDis(request):
    water_dis = WaterModel.objects.all().filter(pk=2)
    documentTypes = WaterModelDocDisposal.objects.all()
    return render(request, 'informations/info_index_waterdis.html', {'dis': water_dis, 'document': documentTypes})


def Informations(request):
    idx = WaterModel.objects.all().filter(pk=3)
    infoDoc = InfoModelDoc.objects.all()
    infoDocLast = InfoModelDocLast.objects.all()
    infoDocforeLast = InfoModelDocbeforeLast.objects.all()
    infoDocforenazLast = InfoModelDocnazLast.objects.all()
    context = {'idx': idx,
               'infoDoc': infoDoc,
               'infoDocLast': infoDocLast,
               'infoDocforeLast': infoDocforeLast,
               'infoDocforenazLast': infoDocforenazLast
               }
    return render(request, 'informations/info_index_section.html', context)
