from django.shortcuts import render
from django.http import HttpResponse

from .models import WaterModel, WaterModelDoc, WaterModelDocDisposal, InfoModelDoc, InfoModelDocLast, InfoModelDocbeforeLast, InfoModelDocnazLast, indxpages, IndexPost
# Create your views here.


#Новости
def CNNpages(request):
    index__ = IndexPost.objects.all().order_by('-pk')
    context = {'index': index__}
    return render( request, 'informations/info__post.html',context)

def show_post(request, post_id):
    index__ = IndexPost.objects.all().filter(pk=post_id)
    return render( request, 'informations/info__post__id.html',{'index': index__})
#Новости

def InfoPagesIdx(request):
    index__ = indxpages.objects.all().filter(pk=1)
    return render(request, 'informations/index.html', {'index': index__})

def InfoPagesVakans(request):
    index__ = indxpages.objects.all().filter(pk=7)
    return render(request, 'informations/index.html', {'index': index__})

def InfoPagesPolitika(request):
    index__ = indxpages.objects.all().filter(pk=8)
    return render(request, 'informations/index.html', {'index': index__})

def InfoPagesNormativ(request):
    Normativ__ = indxpages.objects.all().filter(pk=3)
    return render(request, 'informations/index.html', {'index': Normativ__})


def InfoPagesContact(request):
    index__ = indxpages.objects.all().filter(pk=2)
    return render(request, 'informations/index.html', {'index': index__})


def WaterSupply(request):
    WaterSupp = WaterModel.objects.all().filter(pk=1)
    documentTypes = WaterModelDoc.objects.all().order_by('-pk')
    return render(request, 'informations/info_index_watersupply.html', {'waterpages': WaterSupp, 'document': documentTypes})


def WaterConnect_Polevoy(request):
    water_dis = WaterModel.objects.all().filter(pk=4)
    return render(request, 'informations/info_index_waterconnect_Polevoy.html', {'waterpages': water_dis})

def WaterDis(request):
    water_dis = WaterModel.objects.all().filter(pk=2)
    documentTypes = WaterModelDocDisposal.objects.all().order_by('-pk')
    return render(request, 'informations/info_index_waterdis.html', {'dis': water_dis, 'document': documentTypes})


def Informations(request):
    idx = WaterModel.objects.all().filter(pk=3)
    infoDoc = InfoModelDoc.objects.all().order_by('-pk')
    infoDocLast = InfoModelDocLast.objects.all().order_by('-pk')
    infoDocforeLast = InfoModelDocbeforeLast.objects.all().order_by('-pk')
    infoDocforenazLast = InfoModelDocnazLast.objects.all().order_by('-pk')
    context = {'idx': idx,
               'infoDoc': infoDoc,
               'infoDocLast': infoDocLast,
               'infoDocforeLast': infoDocforeLast,
               'infoDocforenazLast': infoDocforenazLast
               }
    return render(request, 'informations/info_index_section.html', context)
