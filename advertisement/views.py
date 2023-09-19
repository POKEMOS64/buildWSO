from django.shortcuts import render

from .models import advert, advertText
# Create your views here.


def AdvertView(request):
    adverttextviews = advertText.objects.all()
    advertviews = advert.objects.all()
    context = {'text': adverttextviews, 'advertviews': advertviews}
    return render(request, 'advert/cnn_pages.html', context)
