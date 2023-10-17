from django.shortcuts import render
import io
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from kvit.models import Receipt
import tempfile
import time
from django.http import FileResponse, HttpResponse

from qr_code.qrcode.maker import make_qr
from qr_code.qrcode.utils import QRCodeOptions

import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.lib.pagesizes import A5
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.lib.utils import ImageReader
from ls.models import LsModels
# Create your views here.


def pdfLove(request):
    # 406373
    # 106206
    # 514332
    lsKV = LsModels.objects.all().filter(ls='600008')
    uslugi_legends = {
        '1': "Вид \n услуги",
        '2': 'Способ \n учета',
        '3': 'Индив. \n потребление \n (m3)',
        '4': 'Тариф \n (руб.)',
        '5': 'Начисление \n за расч. \n период \n (руб.)',
        '6': 'Перерасчет',
        '7': 'ПК 1.5 \n (руб.)',
        '8': 'К оплате за расч. \n период \n (руб.)',
        '9': 'На начало расчет. периода  (долг"+"/переплата"-") период  (руб.)',
        '10': 'Итого \n к оплате (руб.)'
    }
    info = {
        'adr': "Комарова, д. 134/1, тел. 62-00-38, 68-79-92",
        'post': 'mkdkomarova@bal-vod.ru, mkdkomarova@yandex.ru',
        'graf': "Понедельник с 13:00 до 17:00, Вторник с 08:00 до 17:00 обед с 12:00 до 13:00, Среда с 13:00 до 19:00, \n Четверг: не приемный день, Пятница с 08:00 до 12:00",
        'phone': "68-79-92",
        'srok': "10.07.2023"
    }
    infoChet = {
        '1': '№ пр.учета',
        '2': 'Показания счетчика',
        '3': 'Номер прибора',
        '4': '',
        '5': 'Годен',
    }
    key = {}
    for i in lsKV:

        buffer = io.BytesIO()
        swift = canvas.Canvas(buffer, pagesize=landscape(A5))
        pdfmetrics.registerFont(TTFont('Roboto', 'static/font/Roboto-Light.ttf'))
        pdfmetrics.registerFont(TTFont('RobotoBold', 'static/font/Roboto-Black.ttf'))
        pdfmetrics.registerFont(TTFont('RobotoThin', 'static/font/Roboto-Thin.ttf'))
        # I = Image('static/img/logo.jpg')
        # I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
        # I.drawWidth = 1.25*inch

        swift.setFont('RobotoBold', 10)
        swift.drawString(20, 392, "Счет-извещения")
        swift.setFont('Roboto', 8)
        swift.drawString(140, 392, "за октябрь 2023")
        swift.setFont('Roboto', 7)
        swift.drawString(20, 380, "Получатель: " +  i.org)
        swift.drawString(20, 370, i.innkpp)
        swift.drawString( 20, 360, "р/c: "+ i.rsch )
        swift.drawString( 30, 350, "в " + i.bank  +", БИК: " + i.bic)
        swift.drawString(
                20, 340, "р/c: 40702810956000085886")
        swift.drawString(
                30, 330, "Поволжский Банк ПАО Сбербанк, БИК 043601607")
        swift.line(20, 320, 250, 320)
        swift.line(20, 240, 250, 240)
        swift.line(18, 238, 250, 238)
        swift.line(250, 320, 250, 240)
        swift.line(20, 240, 20, 320)
        swift.line(18, 238, 18, 320)
        
        swift.setFont('RobotoBold', 8)
        swift.drawString(30, 280, i.fio)
        swift.drawString(105, 270,i.ls)
        swift.drawString(30, 300, i.adr )
        swift.drawString(138, 260, i.o_s + " кв.м")
        swift.drawString(130, 250, i.kol_prog)
        swift.drawString(265, 280, "Всего к оплате: ")
        swift.setFont('RobotoBold', 10)
        swift.drawString(270, 250, i.koplate + ' руб.')


        swift.line(260, 265, 260, 240)
        swift.line(340, 265, 340, 240)


        swift.setFont('Roboto', 8)
        swift.drawString(25, 310, "Адрес потребителя: ")
        swift.drawString(25, 290, "Ф.И.О. потребителя: ")
        swift.drawString(25, 270, "Л/счет потребителя: ")
        
        swift.drawString(
                25, 260, "Площадь жилого помещения: ")
        swift.drawString(
                25, 250, "Количество проживающих: ")
        # -----------------------------------
        
        swift.setFont('Roboto', 7)
        # swift.drawString(20, 260, "Пункт приема: " + info['adr'])
        # swift.drawString(20, 250, "Адрес эл.почты: " + info['post'])
        # swift.drawString(20, 240, "Телефон для передачи показаний: " +
                            # info['phone'] + "     Срок оплаты до " + info['srok'])
        # Таблица Платежей-----------------------------------------------------
        p0 = ParagraphStyle('title', fontName='RobotoBold', leading=8, fontSize=6)
        Data__ = [[Paragraph('№ пр.учета',p0),Paragraph('Показания счетчика',p0),'',Paragraph('Номер прибора',p0),Paragraph('Годен',p0)],
                  ['', 'Пред.', 'Тек.', '',''],
                  ]
        if i.name_met1:
            Data__.append([i.name_met1,i.cou_met1,'',i.n_met1,i.date_met1
                        ])
        if i.name_met2:
            Data__.append([i.name_met2,i.cou_met2,'',i.n_met2,i.date_met2
                        ])
        if i.name_met3:
            Data__.append([i.name_met3,i.cou_met3,'',i.n_met3,i.date_met3
                        ])
        if i.name_met4:
            Data__.append([i.name_met4,i.cou_met4,'',i.n_met4,i.date_met4
                        ])
        if i.name_met5:
            Data__.append([i.name_met5,i.cou_met5,'',i.n_met5,i.date_met5
                        ])
        if i.name_met6:
            Data__.append([i.name_met6,i.cou_met6,'',i.n_met6,i.date_met6
                        ])
        swift.drawString(10, 30, str(len(Data__)))
        
        rowHeight__ = len(Data__)
        countres__ = Table(Data__, colWidths=[20*mm]*1 +
            [13*mm]*2 + [20*mm]*1 + [14*mm]*1, rowHeights=[5*mm]*rowHeight__
            )
        # countres__ = Table(Data__)
        
        countres__.setStyle(TableStyle([
                ('FONT', (0, 0), (-1, -1), 'Roboto'),
                ("FONTSIZE", (0, 1), (-1, -1), 6),
                ('ALIGNMENT', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), "TOP"),
                ('VALIGN', (0, 0), (9, 1), "MIDDLE"),
                # ('BACKGROUND', (1, 0), (1, 1), colors.green),
                # ('TEXTCOLOR', (0,0),(1,-1), colors.red),
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('SPAN', (0, 0), (0, 1)),
                ('SPAN', (1, 0), (2, 0)),
                ('SPAN', (3, 0), (3, 1)),
                ('SPAN', (4, 0), (4, 1)),
                ]))

        countres__.wrapOn(swift, 100, 300)
        width2, height3 = countres__.wrapOn(swift, 100, 113)
        countres__.drawOn(swift, 350,  405 - height3, 0)
        # Таблица Платежей-----------------------------------------------------
        p0 = ParagraphStyle('title', fontName='Roboto', leading=8, fontSize=6)
        def f_s(param):
            result = Paragraph(param, p0)
            return result

        zag_lov = []
        for x in range(11):
            if x == 0:
                continue
            x = str(uslugi_legends.get(str(x)))
            res_P = f_s(x)
            zag_lov.append(res_P)
        # Виды услуг
        swift.setFont('Roboto', 8)
        # Услуги

       

        data = [zag_lov,
                ['', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', ''],
                [1, 2, 3, 4, "5 = 3*4", 6, 7, "8 = 5 + 6 + 7", 9, "10 = 8 + 9"],
                ]
        #---------------------------------------/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        # --------------------------/*/*/*/*/*/*/*/*/*/*/*/************/*/*/*/*/*/*/

        def Biling(st,h,*args):
            lsKV = LsModels.objects.all().filter(ls='600008')
            for it__ in lsKV:
                ch__ = it__.name_met1
            UsList = [st]
            for  numb,i in enumerate(args):
                if numb == 0:
                    if ch__:
                        i = '----'
                    else:
                        i = i[:-3]
                UsList.append(i)
            if UsList[6] == 'м3':
                UsList[6] = 0
            else:
                UsList[6] = '0.00'
            if st == 'Водоснабжение' or st == "Водоотведение ГВС":
                UsList[6] = h
            kOplt__ = float(UsList[4]) + float(UsList[5]) + float(UsList[6])
            UsList[7] = kOplt__
            return UsList
        #---------------------------------------/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        if i.nach_11:
            data.append(
                Biling(i.nach_11,i.nach_101, i.nach_31,i.nach_41, i.nach_51, i.nach_61, i.nach_71, i.nach_21, i.nach_81, i.nach_91)
                )
        
        if i.nach_12:
            data.append(
                Biling(i.nach_12,i.nach_102, i.nach_32,i.nach_42, i.nach_52, i.nach_62, i.nach_72, i.nach_22, i.nach_82, i.nach_92)
                )
        
        if i.nach_13:
            data.append(
                Biling(i.nach_13,i.nach_103, i.nach_33,i.nach_43, i.nach_53, i.nach_63, i.nach_73, i.nach_23, i.nach_83, i.nach_93)
                )
        if i.nach_14:
            data.append(
                Biling(i.nach_14,i.nach_104, i.nach_34,i.nach_44, i.nach_54, i.nach_64, i.nach_74, i.nach_24, i.nach_84, i.nach_94)
                )
        if i.nach_25:
            data.append(
                Biling(i.nach_25,i.nach_105, i.nach_35,i.nach_45, i.nach_55, i.nach_65, i.nach_75, i.nach_25,i.nach_85, i.nach_95)
                )
        if i.nach_16:
            data.append(
                Biling(i.nach_26,i.nach_106, i.nach_36,i.nach_46, i.nach_56,i.nach_66, i.nach_76, i.nach_26,i.nach_86, i.nach_96)
                )
        if i.nach_27:
            data.append(
                Biling(i.nach_27,i.nach_107, i.nach_37,i.nach_47, i.nach_57, i.nach_67, i.nach_77, i.nach_27, i.nach_87, i.nach_97)
                )
        if i.nach_28:
            data.append(
                Biling(i.nach_28,i.nach_108, i.nach_38,i.nach_48, i.nach_58, i.nach_68, i.nach_78, i.nach_28,i.nach_88, i.nach_98 )
                )
        if i.nach_19:
            data.append(
                Biling(i.nach_19,i.nach_109, i.nach_39,i.nach_49, i.nach_59, i.nach_69, i.nach_79, i.nach_29, i.nach_89, i.nach_99)
                )
        if i.nach_110:
            data.append(
                Biling(i.nach_110,i.nach_1010,i.nach_210, i.nach_310,i.nach_410, i.nach_510, i.nach_610, i.nach_710, i.nach_810, i.nach_910)
                )
        if i.nach_111:
            data.append(
                Biling(i.nach_111,i.nach_1011,i.nach_211, i.nach_311,i.nach_411, i.nach_511, i.nach_611, i.nach_711, i.nach_811,i.nach_911)
                )
        if i.nach_112:
            data.append(
                Biling(i.nach_112,i.nach_1012,i.nach_212, i.nach_312,i.nach_412, i.nach_512, i.nach_612, i.nach_712, i.nach_812, i.nach_912,)
                )
        if i.nach_113:
            data.append(
                Biling(i.nach_113,i.nach_1013,i.nach_213, i.nach_313,i.nach_413, i.nach_513, i.nach_613, i.nach_713, i.nach_813, i.nach_913)
                )
        if i.nach_114:
            data.append(
                Biling(i.nach_114,i.nach_1014,i.nach_214, i.nach_314,i.nach_414, i.nach_514,i.nach_614, i.nach_714, i.nach_814,i.nach_914,)
                )
        data.append(['Итого: ',i.it_sumnach, i.it_sumpeni, i.it_dolg,i.it_opl, i.pred_plat])
        # Услуги
        
        
        print()
        swift.drawString(10, 10, str(len(data) - 2))
        rowHeight__ = len(data) - 2
        uslugi = Table(data, colWidths=[25*mm]*1 +
            [15*mm]*2 +
            [12*mm]*1 +
            [17*mm]*4 +
            [27*mm]*1 +
            [20*mm]*1, rowHeights=[5*mm]*2 + [5*mm]*rowHeight__
            )
            
        uslugi.setStyle(TableStyle([
                ('FONT', (0, 0), (-1, -1), 'Roboto'),
                ("FONTSIZE", (0, 1), (-1, -1), 6),
                ("FONTSIZE", (0, 0), (9, 1), 1),
                ('ALIGNMENT', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), "TOP"),
                ('VALIGN', (0, 0), (9, 1), "MIDDLE"),
                # ('BACKGROUND', (1, 0), (1, 1), colors.green),
                # ('TEXTCOLOR', (0,0),(1,-1), colors.red),
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
        uslugi.setStyle(TableStyle([
                ('SPAN', (0, 0), (0, 2)),
                ('SPAN', (1, 0), (1, 2)),
                ('SPAN', (2, 0), (2, 2)),
                ('SPAN', (3, 0), (3, 2)),
                ('SPAN', (4, 0), (4, 2)),
                ('SPAN', (5, 0), (5, 2)),
                ('SPAN', (6, 0), (6, 2)),
                ('SPAN', (7, 0), (7, 2)),
                ('SPAN', (8, 0), (8, 2)),
                ('SPAN', (9, 0), (9, 2)),
        ]))
        uslugi.wrapOn(swift, 400, 300)
        width2, height2 = uslugi.wrapOn(swift, 400, 113)
        uslugi.drawOn(swift, 20,  215 - height2, 0)
        # Таблица Платежей-----------------------------------------------------
        # QR-New
        dopInfo = 'Acc=' + i.ls + '|LastName=' + i.fio + '|payerAddress=' + i.adr
        qrw = QrCodeWidget(i.qr + dopInfo + i.qr1)
        b = qrw.getBounds()
        w = b[2]-b[0]
        h = b[3]-b[1]
        d = Drawing(60, 60, transform=[90./w, 0, 0, 90./h, 0, 0])
        d.add(qrw)
        renderPDF.draw(d, swift, 255, 310)
        # QR-New
    swift.showPage()
    swift.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename="hello.pdf")

def landscape(pagesize):
    """Переворачиваем страницу в альбомный режим"""
    a, b = pagesize
    if a < b:
        return (b, a)
    else:
        return (a, b)
def GenKvitUniversal(val,lic):
    uslugi_legends = {
        '1': "Вид \n услуги",
        '2': 'Способ \n учета',
        '3': 'Индив. \n потребление \n (m3)',
        '4': 'Тариф \n (руб.)',
        '5': 'Начисление \n за расч. \n период \n (руб.)',
        '6': 'Перерасчет',
        '7': 'ПК 1.5 \n (руб.)',
        '8': 'К оплате за расч. \n период \n (руб.)',
        '9': 'На начало \n расче. периода \n (долг "+"/переплата "-") \n период \n (руб.)',
        '10': 'Итого \n к оплате (руб.)'
    }
    info = {
        'adr': "Комарова, д. 134/1, тел. 62-00-38, 68-79-92",
        'post': 'mkdkomarova@bal-vod.ru, mkdkomarova@yandex.ru',
        'graf': "Понедельник с 13:00 до 17:00, Вторник с 08:00 до 17:00 обед с 12:00 до 13:00, Среда с 13:00 до 19:00, \n Четверг: не приемный день, Пятница с 08:00 до 12:00",
        'phone': "68-79-92",
        'srok': "10.07.2023"
    }
    
    buffer = io.BytesIO()
    swift = canvas.Canvas(val + lic +'.pdf', pagesize=landscape(A5))
    
    swift.drawString(30, 392, "Счет-извещения")
    swift.drawString(140, 392, "за октябрь 2023")
    swift.drawString(20, 380, 'Индентификатор ПД: ------------------')
    swift.drawString(20, 370, 'Единый ЛС: -------- код ЖКУ: ------------')
    swift.drawString(20, 360, "Получатель: ")
    swift.drawString(20, 350, '-------')
    swift.drawString(
            20, 340, "р/c: "+ "000000" +' в ' + "00000" + "БИК: " + "0000")
    swift.line(20, 325, 310, 325)
    swift.line(20, 270, 310, 270)
    swift.line(310, 325, 310, 270)
    swift.line(20, 325, 20, 270)
    swift.drawString(25, 315, "Адрес потребителя: "+ "Adres")
    swift.drawString(25, 305, "Ф.И.О. потребителя: "+ "FIO")
    swift.drawString(25, 295, "Л/счет потребителя: "+ "0110100")
    swift.drawString(
            25, 285, "Площадь жилого помещения: "+ "43,5" + " кв.м")
    swift.drawString(
            25, 275, "Количество проживающих: " + '5')
    # -----------------------------------
    swift.drawString(20, 260, "Пункт приема: " + info['adr'])
    swift.drawString(20, 250, "Адрес эл.почты: " + info['post'])
    swift.drawString(20, 240, "Телефон для передачи показаний: " +
                        info['phone'] + "     Срок оплаты до " + info['srok'])
    # Таблица Платежей-----------------------------------------------------
    p0 = ParagraphStyle('title', leading=8, fontSize=6)
    def f_s(param):
        result = Paragraph(param, p0)
        return result

    zag_lov = []
    for i in range(11):
        if i == 0:
            continue
        i = str(uslugi_legends.get(str(i)))
        res_P = f_s(i)
        zag_lov.append(res_P)
    # Виды услуг
    nach_obj_1LIST = []

    data = [zag_lov,
            ['', '', '', '', '', '', '', '', ''],
            [1, 2, 3, 4, "5 = 3*4", 6, 7, "8 = 5 + 6 + 7", 9, "10 = 8 + 9"],
            ]
    uslugi = Table(data, colWidths=[25*mm]*1 +
        [15*mm]*2 +
        [10*mm]*1 +
        [15*mm]*3 
        # + [25*mm]*1, rowHeights=[5*mm]*2 + [4*mm]*11
        )
    uslugi.setStyle(TableStyle([

            ("FONTSIZE", (0, 0), (-1, -1), 6),
            ('ALIGNMENT', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), "TOP"),
            ('VALIGN', (0, 0), (8, 1), "MIDDLE"),
            # ('BACKGROUND', (1, 0), (1, 1), colors.green),
            # ('TEXTCOLOR', (0,0),(1,-1), colors.red),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('SPAN', (0, 0), (0, 1)),
            ('SPAN', (1, 0), (1, 1)),
            ('SPAN', (2, 0), (2, 1)),
            ('SPAN', (3, 0), (3, 1)),
            ('SPAN', (4, 0), (4, 1)),
            ('SPAN', (5, 0), (5, 1)),
            ('SPAN', (6, 0), (6, 1)),
            ('SPAN', (7, 0), (7, 1)),
            ('SPAN', (8, 0), (8, 1)),
            ]))
    uslugi.wrapOn(swift, 400, 300)
    width2, height2 = uslugi.wrapOn(swift, 400, 113)
    uslugi.drawOn(swift, 20,  230 - height2, 0)
    # Таблица Платежей-----------------------------------------------------
    # QR-New
    qrw = QrCodeWidget("Checking the text - Проверка текста")
    b = qrw.getBounds()
    w = b[2]-b[0]
    h = b[3]-b[1]
    d = Drawing(45, 45, transform=[60./w, 0, 0, 60./h, 0, 0])
    d.add(qrw)

    renderPDF.draw(d, swift, 270, 345)
    swift.showPage()
    swift.save()

def GenKvit(val,lic):
    p = canvas.Canvas(val + lic +'.pdf')
    p.drawString(100,500,"Тест PDF")
    p.showPage()
    p.save()

def Mail(request):
    assem = Receipt.objects.all()
    ListTuple = []
    LicList = []
    for i in assem:
        userX = i.user_name
        MailX = i.email_pole
        LicList = [i.lic1_pole,
                   i.lic2_pole,
                   i.lic3_pole,
                   i.lic4_pole,
                   i.lic5_pole,
                   i.lic6_pole
                   ]
        ListTrue = [
            i.lic11_pole,
            i.lic12_pole,
            i.lic13_pole,
            i.lic14_pole,
            i.lic15_pole,
            i.lic16_pole
        ]
        print(LicList)
        ListTuple.append(MailX)
    datatuple = len(ListTuple)
    i = 0
    
    while i < datatuple:
        time.sleep(2) 
        for x in range(6):
            ListTuple__ = ListTuple[i]
            path = str('kvitres/' + MailX)
            if True == ListTrue[x]:
                LicList__ = "Электронная квитанция Лицевой счет Макет задержка 2мс:" + str(LicList[x])
                print(True)
                print(ListTuple__)
                GenKvitUniversal(path,str(LicList[x]))
                email = EmailMessage(
                    LicList__,
                    'Электронная квитанция за октябрь',
                    settings.DEFAULT_FROM_EMAIL,
                    [ListTuple__],
                    reply_to= ['bot@bal-vod.ru'],
                    headers={'Message': 'test'}
                )
                email.attach_file(path + str(LicList[x]) + '.pdf')
                email.send()
                time.sleep(1)   
        i += 1
    return render(request, 'mail/send.html')
