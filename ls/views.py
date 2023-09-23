from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
from ls.models import LsModels, mkdLsList, selaLsList, chLsList
from ls.forms import LkInduc
from users.forms import MakeStatement
from inducations.models import InduImport, InduExport, InduExportSela, InduExportCH
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
    messadges = ''
    messages__=''
    datavhod = ''
    form__ = MakeStatement()
    form = LkInduc()
    ls = ''
    # ------------ Таблицы---------------------
    if request.method == 'POST':
        form = MakeStatement(data=request.POST)
        id_lsPOST = request.POST['id_ls']
        name_domPOST = request.POST['name_dom']
        name_kvPOST = request.POST['name_kv']

        mkdLS = mkdLsList.objects.filter(id_ls=request.POST['id_ls'])
        selaLS = selaLsList.objects.filter(id_ls=request.POST['id_ls'])
        chLS = chLsList.objects.filter(id_ls=request.POST['id_ls'])

        mkdLS__ = InduExport.objects.filter(id_ls=request.POST['id_ls'])
        selaLS__ = InduExportSela.objects.filter(id_ls=request.POST['id_ls'])
        chLS__ = InduExportCH.objects.filter(id_ls=request.POST['id_ls'])
        if mkdLS:
            SEND_ = InduExport
            messadges = 'Передача показаний в МКД'
            DRAW = mkdLS__
            print('Есть', messadges)
        elif selaLS:
            SEND_ = InduExportSela
            messadges = 'Передача показаний в Село'
            DRAW = selaLS__
            print('Есть', messadges)
        elif chLS:
            SEND_ = InduExportCH
            messadges = 'Передача показаний в Частный сектор'
            DRAW = chLS__
            print('Есть', messadges)
        else:
            messadges = 'Показания не найдены в текущем месяце.'
        
        if DRAW:
            print('Есть', messadges)
        else:
            if 'lslogin' in request.POST:
                if form.is_valid():
                    page_ls_dan = InduImport.objects.filter(id_ls=id_lsPOST, name_dom=name_domPOST, name_kv=name_kvPOST)
                    print(page_ls_dan)
                else:
                    messages__ = 'Данные не найдены, попробуйте еще раз!'
            elif 'inducenter' in request.POST:
                datavhod = InduImport.objects.filter(id_ls=id_lsPOST, name_dom=name_domPOST, name_kv=name_kvPOST)
                if datavhod:
                    datavhod = InduImport.objects.all().filter(id_ls=id_lsPOST)
                else:
                    datavhod = ''
                    messages = "Для этого лицевого, нет данных для заполнения."
                if form.is_valid():
                    __hv1_data = form.cleaned_data['hv1_data']
                    __gv1_data = form.cleaned_data['gv1_data']
                    __hv2_data = form.cleaned_data['hv2_data']
                    __gv2_data = form.cleaned_data['gv2_data']
                    __hv3_data = form.cleaned_data['hv3_data']
                    __gv3_data = form.cleaned_data['gv3_data']
                    __hv_data = form.cleaned_data['hv_data']
                    __gv4_data = form.cleaned_data['gv4_data']
                    for obj in datavhod:
                        id_ls = obj.id_ls
                        name_dom = obj.name_dom
                        name_kv = obj.name_kv
                        feed = SEND_(
                            id_ls=id_ls,
                            name_dom=name_dom,
                            name_kv=name_kv,
                            codsch_hv1=obj.codsch_hv1,
                            hv1_data=__hv1_data,
                            codsh_gv1=obj.codsh_gv1,
                            gv1_data=__gv1_data,
                            codsch_hv2=obj.codsch_hv2,
                            hv2_data=__hv2_data,
                            codsch_gv2=obj.codsch_gv2,
                            gv2_data=__gv2_data,
                            codsch_hv3=obj.codsch_hv3,
                            hv3_data=__hv3_data,
                            codsch_gv3=obj.codsch_gv3,
                            gv3_data=__gv3_data,
                            codsch_hv4=obj.codsch_hv4,
                            hv_data=__hv_data,
                            codsh_gv4=obj.codsh_gv4,
                            gv4_data=__gv4_data
                        )
                        feed.save()
                        return HttpResponseRedirect(reverse('users:profile'))

                else:
                    form__ = MakeStatement()
                    print("Робот")

    context = {'form': form,
               'page_ls_dan': page_ls_dan, 'messages': messages,'messages__':messages__}
    return render(request, 'ls/indx.html', context)
