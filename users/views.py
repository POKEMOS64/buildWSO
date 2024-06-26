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

# def UserSerialize(request):
#     userProfile = User.objects.all()
#     for x in userProfile:
#         if x == round('Routings'):
#             break

#     def build(self,*args, **kwargs)
#         self.username = ''
#         return
#     if __name__ == '__main__':
#         pass

#     # context = {
#     #     ''
#     # }
#     return render(request)


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
    OverPay = 'off'
    LSData__List__summa__ = ''

    def Constructor(val):
        List = []
        type__ = ''
        for i in val:
            if i == '-':
                type__Prelod = '1'
                continue

            elif i == ',':
                i = "."
                type__ = '1'
            List.append(i)
        List_ = List
        itItog = str(List_).replace('[', '').replace("]", '').replace(
            "'", "").replace(',', '').replace(' ', '')
        if type__ == '1':
            res = float(itItog)
            print(type__)
        else:
            res = int(itItog)

        return res

    def KillerString(val):
        List = []
        type__ = ''
        for i in val:
            if i == '-':
                continue
            elif i == ',':
                i = "."
                type__ = '1'
            List.append(i)
        List_ = List
        itItog__ = str(List_).replace('[', '').replace("]", '').replace(
            "'", "").replace(',', '').replace(' ', '')

        if type__ == '1':
            res = float(itItog__)
            print(type__)
        else:
            itItog = itItog__ + '.00'
            res__ = itItog
            print(res__)
            res = float(res__)
        return res

    def Constructor__Plus(val, value):
        L__ = []
        L = ''
        res__x = ''
        resultat__ = ''

        def Constructor_x(value__):
            List = []
            type__ = ''
            for i in value__:
                if i == '-':
                    type__Prelod = '1'
                    continue

                elif i == ',':
                    i = "."
                    type__ = '1'
                List.append(i)
            List_ = List
            itItog = str(List_).replace('[', '').replace("]", '').replace(
                "'", "").replace(',', '').replace(' ', '')
            print(itItog)
            if type__ == '1':
                res = float(itItog)
                print(type__)
            else:
                itItog = itItog + '.00'
                res__ = itItog
                print(res__)
                res = float(res__)
            return res

        if val == None:
            res__ = float(100000)
        elif isinstance(val, float):
            res__ = val
            print(res__)
        else:
            for i in val:
                if i == ',':
                    i = '.'
                L__.append(i)
            L = str(L__).replace('[', '').replace(']', '').replace(
                ',', '').replace("'", "").replace(' ', '')
            val = L
            res__ = float(val)
            print(res__)

        resultat__ = Constructor_x(value)
        data_1 = res__
        if data_1 >= resultat__:
            res__x = '1'
        else:
            res__x = '0'
        res = res__x

        return res

    for obj in LSData__List:
        make = obj.qr
        dopInfo = '|LastName=' + obj.fio + '|payerAddress=' + obj.adr
        for i in obj.koplate:
            if i[0] == '-':
                OverPay = 'On'
                print(obj.it_dolg)
        itDolg = Constructor(obj.it_dolg)
        itOpl = Constructor(obj.koplate)
        itSumnach = Constructor(obj.it_sumnach)
        LSData__List__summa__ = str(round(itOpl, 2))
        info1 = obj.qr1
    qr_Options = QRCodeOptions(
        size='6', border=3, dark_color='#1f1f57', light_color='#fff', data_dark_color="#038ED1", quiet_zone_color='#fff', error_correction='L')
    if LSData__List:
        qrMake = make + dopInfo + info1
    else:
        qrMake = 'Нужно выбрать или добавить лицевой счет для отображения суммы.'
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
        messages_ = '----'
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
    value = ''
    mess_data = ''
    messadges = ''
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
        # print(form__)
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
                hv1_data = Constructor__Plus(__hv1_data, obj.hv1_data)
                hv2_data = Constructor__Plus(__hv2_data, obj.hv2_data)
                hv3_data = Constructor__Plus(__hv3_data, obj.hv3_data)
                hv4_data = Constructor__Plus(__hv_data, obj.hv_data)
                gv1_data = Constructor__Plus(__gv1_data, obj.gv1_data)
                gv2_data = Constructor__Plus(__gv2_data, obj.gv2_data)
                gv3_data = Constructor__Plus(__gv3_data, obj.gv3_data)
                gv4_data = Constructor__Plus(__gv4_data, obj.gv4_data)
                if hv1_data == '0':
                    mess_data = 'Ошибка ХВ_1'
                    messadges = '1'
                    form__ = MakeStatement()
                elif hv2_data == '0':
                    mess_data = 'Ошибка ХВ_2'
                    messadges = '1'
                    form__ = MakeStatement()
                elif hv3_data == '0':
                    mess_data = 'Ошибка ХВ_3'
                    messadges = '1'
                    form__ = MakeStatement()
                elif hv3_data == '0':
                    mess_data = 'Ошибка ХВ_3'
                    messadges = '1'
                    form__ = MakeStatement()
                elif hv4_data == '0':
                    mess_data = 'Ошибка ХВ_4'
                    messadges = '1'
                    form__ = MakeStatement()
                elif gv1_data == '0':
                    mess_data = 'Ошибка ГВС_1'
                    messadges = '1'
                    form__ = MakeStatement()
                elif gv2_data == '0':
                    mess_data = 'Ошибка ГВС_2'
                    messadges = '1'
                    form__ = MakeStatement()
                elif gv3_data == '0':
                    mess_data = 'Ошибка ГВС_3'
                    messadges = '1'
                    form__ = MakeStatement()
                elif gv4_data == '0':
                    mess_data = 'Ошибка ГВС_4'
                    messadges = '1'
                    form__ = MakeStatement()
                else:
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

    context = {"form": form,
               'form__': form__,
               'profile_user': profile_user,
               'messages': mess_data,
               'datavhod': datavhod,
               'Error': messadges,
               'dataExport': DRAW,
               'messages_': messages_,
               'LSData': LSData__List,
               'LSData__List__summa': LSData__List__summa__,
               'OverPay': OverPay,
               'qrMake': qrMake,
               'qr_Options': qr_Options,
               'Error': messadges,
               'mess_data': mess_data,
               }
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
            summ_ = request.POST['summ_'].replace('.', ',')
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
                            messages = "Ваш лицевой счет " + fac_lis + ' добавлен'
                            break
                        else:
                            messages = "Вы добавили максимально количество лицевых для Вашего профиля " + \
                                fac_lis + ' не добавлен'
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
                messages = 'Такой лицевой счет не найден (Оплата еще не зашла). Попробуйте добавить другой'
                form_ = AddLis()
        else:
            print("Не работает")
    else:
        form_ = AddLis()
    context = {'forma': form_, 'messages': messages}
    return render(request, 'users/licadd.html', context)
