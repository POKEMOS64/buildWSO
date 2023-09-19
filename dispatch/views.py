from django.shortcuts import render

from .models import dispatch, dispatchText
# Create your views here.


def dispatchViews(request):
    dispatchviews = dispatch.objects.all()
    dispatchTextviews = dispatchText.objects.all()
    context = {'text': dispatchTextviews, 'dispahtviews': dispatchviews}
    return render(request, 'dispatch/dispatch_pages.html', context)
