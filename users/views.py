from django.shortcuts import render, HttpResponseRedirect
# Сама магия ТУТ!!
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfilePass, UserProfileFormRed, AddLis, MakeStatement
from ls.forms import ProfileUser
from ls.models import LsModels, selaLsList, chLsList, mkdLsList
from inducations.models import InduImport, InduExport, InduExportSela, InduExportCH
from .models import User, fcecountSQL
# / Сама магия ТУТ!!

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib import auth
from django.views.generic.edit import UpdateView
from django.urls import reverse
from qr_code.qrcode.maker import make_qr
from qr_code.qrcode.utils import QRCodeOptions

# Create your views here.


def bruteUser(profile_user):
    for obj in profile_user:
        username = obj.username
        email = obj.email
        first_name = obj.first_name
        phone = obj.phone
        lic = obj.lic
        lic2 = obj.lic2
        lic3 = obj.lic3
        lic4 = obj.lic4
        lic5 = obj.lic5
        lic6 = obj.lic6
    return (username, email, first_name, phone, lic, lic2, lic3, lic4, lic5, lic6)


def login(request):
    # Если пришел POST запрос, цикл начинается
    if request.method == 'POST':
        # Данные которые отпраляются из формы
        form = UserLoginForm(data=request.POST)
        # Проверяем на валидность
        if form.is_valid():
            # Данные из формы
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    profile = User.objects.get(pk=request.user.pk)
    profile_user = User.objects.filter(pk=request.user.pk)

    datavhod = ''
    messages = ''
    messages_ = ''
    for ob in profile_user:
        tr_ = ob.lic_def
    # ---Все то что отвечает за передачу показаний в таблицы ---

    mkdstatment = InduExport.objects.all()
    selastatment = InduExportSela.objects.all()
    chstatment = InduExportCH.objects.all()

    mkdLS = mkdLsList.objects.filter(id_ls=tr_)
    selaLS = selaLsList.objects.filter(id_ls=tr_)
    chLS = chLsList.objects.filter(id_ls=tr_)

    LSData__List = LsModels.objects.filter(ls=tr_)
    for obj in LSData__List:
        make = obj.qr
        info1 = obj.info1
    qr_Options = QRCodeOptions(
        size='6', border=3, dark_color='#1f1f57', light_color='#fff', data_dark_color="#038ED1", quiet_zone_color='#fff', error_correction='L')

    if LSData__List:
        qrMake = make + info1
    else:
        qrMake = 'Данные не загруженны'
    DRAW = ''
    if mkdLS:
        print('MKD')
        messages_ = 'МКД'
        SEND_ = InduExport
        # Подмена переменной
        DRAW = InduExport.objects.filter(id_ls=tr_)
        # Получаем строку
        DRAW_ = InduExport.objects.all().filter(id_ls=tr_)
        # Выдергиваем все данные
    elif selaLS:
        print('Sela')
        messages_ = 'Село'
        SEND_ = InduExportSela
        DRAW = InduExportSela.objects.filter(id_ls=tr_)
        DRAW_ = InduExport.objects.all().filter(id_ls=tr_)
    elif chLS:
        print('CH')
        messages_ = 'Частный сектор'
        SEND_ = InduExportCH
        DRAW = InduExportCH.objects.filter(id_ls=tr_)
        DRAW_ = InduExportCH.objects.all().filter(id_ls=tr_)
    else:
        messages_ = 'Лицевой счет не определен!!! Сбой'
    # /////Все то что отвечает за передачу показаний в таблицы ---
    # -----------------------------------------------------------------
    datavhod = InduImport.objects.filter(id_ls=tr_)
    if datavhod:
        datavhod = InduImport.objects.all().filter(id_ls=tr_)

    else:
        datavhod = ''
        messages = "Для этого лицевого, нет данных для заполнения."

    # -----------------------------------------------------------------

    # dataExport = InduExport.objects.filter(id_ls=tr_)
    if DRAW:
        DRAW_
    else:
        DRAW
    # -----------------------------------------------------------------
    form = UserProfileForm(instance=profile)
    form__ = MakeStatement()
    if request.method == 'POST' and 'profilels' in request.POST:
        form = UserProfileForm(
            request.POST, request.FILES or None, instance=profile)
        for obj in profile_user:
            username = obj.username
            email = obj.email
            first_name = obj.first_name
            phone = obj.phone
            lic = obj.lic
            lic2 = obj.lic2
            lic3 = obj.lic3
            lic4 = obj.lic4
            lic5 = obj.lic5
            lic6 = obj.lic6
        if form.is_valid():
            face = request.POST['lic_def']
            front = [lic, lic2, lic3, lic4, lic5, lic6]
            for obj in front:
                if face == obj:
                    instance = form.save(commit=False)
                    instance.username = username
                    instance.email = email
                    instance.first_name = first_name
                    instance.phone = phone
                    instance.lic = lic
                    instance.lic2 = lic2
                    instance.lic3 = lic3
                    instance.lic4 = lic4
                    instance.lic5 = lic5
                    instance.lic6 = lic6
                    instance.save()
                    return HttpResponseRedirect(reverse('users:profile'))
            else:
                pass
        else:
            print(form.errors)
    elif request.method == 'POST' and 'datavhod' in request.POST:
        form__ = MakeStatement(data=request.POST)
        if form__.is_valid():
            #     human = True
            __hv1_data = form__.cleaned_data['hv1_data']
            __gv1_data = form__.cleaned_data['gv1_data']
            __hv2_data = form__.cleaned_data['hv2_data']
            __gv2_data = form__.cleaned_data['gv2_data']
            __hv3_data = form__.cleaned_data['hv3_data']
            __gv3_data = form__.cleaned_data['gv3_data']
            __hv_data = form__.cleaned_data['hv_data']
            __gv4_data = form__.cleaned_data['gv4_data']
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
                if DRAW:
                    DRAW.update(
                        hv1_data=__hv1_data,
                        gv1_data=__gv1_data,
                        hv2_data=__hv2_data,
                        gv2_data=__gv2_data,
                        hv3_data=__hv3_data,
                        gv3_data=__gv3_data,
                        hv_data=__hv_data,
                        gv4_data=__gv4_data
                    )
                else:
                    feed.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            form__ = MakeStatement()
            print("Робот")

    else:

        form__ = MakeStatement()
        form = UserProfileForm(instance=profile)

    context = {"form": form, 'form__': form__, 'profile_user': profile_user,
               'messages': messages, 'datavhod': datavhod, 'dataExport': DRAW, 'messages_': messages_, 'LSData': LSData__List, 'qrMake': qrMake, 'qr_Options': qr_Options}
    return render(request, 'users/user.html', context)


def passwordreset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Ваш пароль был успешно обновлен!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже.')
            print(form.errors)
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, 'users/password.html', context)


def profilePers(request):
    profile = User.objects.get(pk=request.user.pk)
    profile_user = User.objects.filter(pk=request.user.pk)
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES or None, instance=profile)
        for obj in profile_user:
            username = obj.username
            email = obj.email
            first_name = obj.first_name
            phone = obj.phone
            lic = obj.lic
            lic2 = obj.lic2
            lic3 = obj.lic3
            lic4 = obj.lic4
            lic5 = obj.lic5
            lic6 = obj.lic6
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = username
            instance.email = email
            instance.lic = lic
            instance.lic2 = lic2
            instance.lic3 = lic3
            instance.lic4 = lic4
            instance.lic5 = lic5
            instance.lic6 = lic6
            instance.save()

            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=profile)
    context = {"form": form, 'profile_user': profile_user}
    return render(request, 'users/userredactor.html', context)


def profileAddLis(request):
    fc__ = '0'
    profile = User.objects.get(pk=request.user.pk)
    profile_user = User.objects.filter(pk=request.user.pk)
    messages = ''
    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES or None, instance=profile)
        form_ = AddLis(data=request.POST)
        if form_.is_valid():
            fac_lis = request.POST['fac_lis']
            summ_ = request.POST['summ_'].replace(',', '.')
            fc__ = fcecountSQL.objects.filter(
                FCNUMBERCOUNT=fac_lis, MAX1=summ_)
            for obj in profile_user:
                username = obj.username
                email = obj.email
                first_name = obj.first_name
                phone = obj.phone
                lic = obj.lic
                lic2 = obj.lic2
                lic3 = obj.lic3
                lic4 = obj.lic4
                lic5 = obj.lic5
                lic6 = obj.lic6
            front = [lic, lic2, lic3, lic4, lic5, lic6]
            if fc__:
                result__ = fcecountSQL.objects.get(FCNUMBERCOUNT=fac_lis)
                for obj, param_ in enumerate(front):
                    if param_ == fac_lis:
                        form_ = AddLis()
                        messages = 'Данный лицевой уже подключен!'
                        break
                    else:
                        if param_ == None:
                            front[obj] = str(result__)
                            messages = "Вас лицевой счет " + fac_lis + ' добавлен'
                            break
                        else:
                            form_ = AddLis()
                res_ = front
                instance = form.save(commit=False)
                instance.username = username
                instance.email = email
                instance.first_name = first_name
                instance.phone = phone
                instance.lic = res_[0]
                instance.lic2 = res_[1]
                instance.lic3 = res_[2]
                instance.lic4 = res_[3]
                instance.lic5 = res_[4]
                instance.lic6 = res_[5]
                instance.save()
            else:
                messages = 'Такой лицевой счет не найден. Попробуйте добавить другой'
                form_ = AddLis()
        else:
            print("Не работает")
    else:
        form_ = AddLis()
    context = {'forma': form_, 'messages': messages}
    return render(request, 'users/licadd.html', context)
