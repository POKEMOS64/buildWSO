from django.shortcuts import render

# Create your views here.
from ls.models import LsModels
from ls.forms import LkInduc
from users.forms import MakeStatement
from inducations.models import InduImport
from users.models import User
from django.urls import reverse
from django.contrib import messages


def LsModelView(request):
    userDB = User.objects.get(username=request.user.username)
    useProf = User.objects.filter(username=userDB)
    page_ls = LsModels.objects.filter(ls=userDB)
    for obj in useProf:
        ls = obj.lic
    context = {'ls': LsModels(), 'page_ls': page_ls,
               'userDB': userDB, 'userProf': ls}

    return render(request, 'ls/index.html', context)


def inducaions(request):
    page_ls_dan = '0'
    messages = ''
    form__ = MakeStatement()
    form = LkInduc(data=request.POST)
    if request.method == 'POST' and 'lslogin' in request.POST:
        form = LkInduc(data=request.POST)
        if form.is_valid():
            id_lsPOST = request.POST['id_ls']
            name_domPOST = request.POST['name_dom']
            name_kvPOST = request.POST['name_kv']
            page_ls_dan = InduImport.objects.filter(
                id_ls=id_lsPOST, name_dom=name_domPOST, name_kv=name_kvPOST)
            if page_ls_dan:
                page_ls_dan = InduImport.objects.all().filter(id_ls=id_lsPOST)
            else:
                messages = 'Такой абонент не найден, попробуйте еще раз.'
                page_ls_dan = '0'
                form = LkInduc()
    elif request.method == 'POST' and 'inducenter' in request.POST:
        form__ = MakeStatement(data=request.POST)
        pass
    else:
        form__ = MakeStatement()
        page_ls_dan = '0'
        form = LkInduc()

    context = {'form': form, 'form__': form__,
               'page_ls_dan': page_ls_dan, 'messages': messages}
    return render(request, 'ls/indx.html', context)
