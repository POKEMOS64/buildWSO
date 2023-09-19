from django.shortcuts import render
from .models import debtCHModel, tamponingModel, debtURModel
# Create your views here.


def debtViews(request):
    debt_human = debtCHModel.objects.all()
    tampon_person = tamponingModel.objects.all()
    debt_private = debtURModel.objects.all()
    context = {'human': debt_human,
               'person': tampon_person, 'private': debt_private}
    return render(request, 'debt/debt_pages.html', context)
