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
# Create your views here.


def pdfLove(request):
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
    swift = canvas.Canvas(buffer, pagesize=landscape(A5))
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
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto.ttf'))
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
