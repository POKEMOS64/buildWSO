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


def ResultViews(request):
    return render(request, 'ls/result.html')


def inducaions(request):

    page_ls_dan = '0'
    messages = ''
    inform__ = ''
    messadges = ''
    messages__ = ''
    datavhod = ''
    mess_data = ''
    form__ = MakeStatement()
    form = MakeStatement()
    ls = ''
    DRAW__ = ''
    # ------------ Таблицы---------------------
    if request.method == 'POST':
        form = MakeStatement(data=request.POST)
        id_lsPOST = request.POST['id_ls']
        name_domPOST = request.POST['name_dom']
        if len(request.POST['name_kv']) < 1:
            name_kvPOST = None
            print(name_kvPOST, 'Joker')
            temp__check = InduImport.objects.filter(
                id_ls=request.POST['id_ls'],
                name_dom=request.POST['name_dom'],
            )
        else:
            name_kvPOST = request.POST['name_kv']
            temp__check = InduImport.objects.filter(
                id_ls=request.POST['id_ls'],
                name_dom=request.POST['name_dom'],
                name_kv=request.POST['name_kv']
            )

        mkdLS = mkdLsList.objects.filter(id_ls=request.POST['id_ls'])
        selaLS = selaLsList.objects.filter(id_ls=request.POST['id_ls'])
        chLS = chLsList.objects.filter(id_ls=request.POST['id_ls'])

        mkdLS__ = InduExport.objects.filter(id_ls=request.POST['id_ls'])
        selaLS__ = InduExportSela.objects.filter(id_ls=request.POST['id_ls'])
        chLS__ = InduExportCH.objects.filter(id_ls=request.POST['id_ls'])
        if mkdLS:
            SEND_ = InduExport
            if temp__check:
                DRAW = mkdLS__
            else:
                DRAW__ = '0'
        elif selaLS:
            SEND_ = InduExportSela
            if temp__check:
                DRAW = selaLS__
            else:
                DRAW__ = '0'
        elif chLS:
            SEND_ = InduExportCH
            if temp__check:
                DRAW = chLS__
            else:
                DRAW__ = '0'
        else:
            DRAW__ = '0'
            messadges = 'Ваш лицевой счет не найден в МУП "Балаково-Водоканал"'

        if DRAW__ == '0':
            inform__ = 'Лицевой счет не найден.'
            form = MakeStatement()
        elif DRAW:
            inform__ = 'Данные уже были внесены ранее.'
            form = MakeStatement()
        else:
            if 'lslogin' in request.POST:
                if form.is_valid():
                    page_ls_dan = InduImport.objects.filter(
                        id_ls=id_lsPOST, name_dom=name_domPOST)
                else:
                    print("Hello")
            elif 'inducenter' in request.POST:
                datavhod = InduImport.objects.filter(
                    id_ls=id_lsPOST, name_dom=name_domPOST)
                if datavhod:
                    datavhod = InduImport.objects.all().filter(id_ls=id_lsPOST)
                else:
                    datavhod = ''
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
                        # if __hv1_data < float(obj.hv1_data):
                        #     messadges = 1
                        #     mess_data = 'Ошибка ХВ_1'
                        #     print('Сработало')
                        # elif __hv2_data < float(obj.hv2_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ХВ_2'
                        # elif __hv3_data < float(obj.hv3_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ХВ_3'
                        # elif __hv_data < float(obj.hv_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ХВ_4'
                        # elif __gv1_data < float(obj.gv1_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ГВС_1'
                        # elif __gv2_data < float(obj.gv2_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ГВС_2'
                        # elif __gv3_data < float(obj.gv3_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ГВС_3'
                        # elif __gv4_data < float(obj.gv4_data):
                        #     messadges = 1
                        #     mess_data ='Ошибка ГВС_4'
                        # else:
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
                        return HttpResponseRedirect(reverse('ls:result'))

                else:
                    form__ = MakeStatement()
                    print("Робот")
            else:
                form__ = MakeStatement()
                print("Робот")
    context = {'form': form,
               'page_ls_dan': page_ls_dan,
               'messages': messages,
               'Error': messadges,
               'messages__': messages__,
               'inform__': inform__,
               'mess_data': mess_data,
               }
    return render(request, 'ls/indx.html', context)
