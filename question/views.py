from django.shortcuts import render, HttpResponseRedirect
from .models import qestionModel, questionAbonModel
from .forms import questForms
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def questViews(request):
    quest = qestionModel.objects.all()
    messages = ''
    if request.method == "POST":
        form = questForms(data=request.POST)
        if form.is_valid():
            human = True
            feed = qestionModel(
                questionItself=form.cleaned_data['questionItself']
            )
            feed.save()
            return HttpResponseRedirect(reverse('question:question'))
        else:
            messages = 'Вы возможно робот.'
    else:
        form = questForms()
    return render(request, 'question/question_pages.html', {'quest': quest, 'form': form, 'messages': messages})
