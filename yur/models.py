from django.db import models

# Create your models here.

class yur(models.Model):
    EA = models.IntegerField(varbose_name='Идентификатор', max_lenght=50, null='True', blank=True)
    inn = models.IntegerField(varbose_name='ИНН', max_lenght=50, null='True', blank=True)
    kpp = models.integerField(verbose_name='КПП', max_lenght=50, null='True', blank=True)
    phone = models.ChartField(verbose_name='Телефон', max_lenght=50, null='True', blank=True)
    data_gogi = models.DateField(verbose-name='Дата договора', null='True', blank=True)
    data_end = models.DateField(verbose-name='Расторгнут', null='True', blank=True)
    name_org = models.ChartField(verbose_name='Наименование предприятия', max_lenght=255, null='True', blank=True)
    name_ruk = models.ChartField(verbose_name='Наименование ФИО Руководителя', max_lenght=255, null='True', blank=True)
    osv = models.ChartField(verbose_name='Основание', max_lenght=255, null='True', blank=True)
    rash = models.ChartField(verbose_name='Расчетный счет', max_lenght=255, null='True', blank=True)
    water = models.ChartField(verbose_name='Объем', max_lenght=100, null='True', blank=True)
    can = models.ChartField(verbose_name='Канализация', max_lenght=100, null='True', blank=True)
    okpo = models.ChartField(verbose_name='ОКПО', max_lenght=255, null='True', blank=True)
    okved = models.ChartField(verbose_name='ОКВЭД/ОКОНХ', max_lenght=255, null='True', blank=True)
    svid = models.ChartField(verbose_name='Свидетельство', max_lenght=255, null='True', blank=True)
    prim = models.ChartField(verbose_name='Доп. поле', max_lenght=255, null='True', blank=True)
    passport = models.ChartField(verbose_name='Паспорт', max_lenght=255, null='True', blank=True)
    email = models.EmailField(max_length=150, verbose_name='е-mail ',null='True', blank=True)
    blank__ = models.ChartField(verbose_name='Наименование бланка', max_lenght=255, null='True', blank=True)
    blank__adr = models.ChartField(verbose_name='Адрес плательщика(Покупателя)', max_lenght=255, null='True', blank=True)
    gruz__ = models.ChartField(verbose_name='Наименование грузопулучателя', max_lenght=255, null='True', blank=True)
    gruz__adr = models.ChartField(verbose_name='Адрес грузополучателя', max_lenght=255, null='True', blank=True)





