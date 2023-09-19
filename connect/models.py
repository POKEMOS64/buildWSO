from django.db import models
from datetime import datetime
from users.models import User


# Create your models here.


def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Connect(models.Model):
    shipped = 1
    inspection = 2
    Executed = 3
    status = [
        (shipped, 'Отправлено'),
        (inspection, 'На проверке'),
        (Executed, 'Исполнено')
    ]
    user = models.ForeignKey(
        null=True, to=User, on_delete=models.SET_NULL)
    pr_Name = models.CharField(
        max_length=250, verbose_name='Фамилия, Имя, Отчество')
    pr_phone = models.CharField(max_length=20, verbose_name='Ваш телефон')
    pr_email = models.EmailField(max_length=150, verbose_name='Ваш е-mail ')
    pr_reg_city = models.CharField(max_length=250, verbose_name='Город')
    pr_reg_street = models.CharField(max_length=200, verbose_name='Улица')
    pr_reg_home = models.CharField(max_length=10, verbose_name='Дом')
    pr_reg_flat = models.PositiveIntegerField(
        max_length=10, verbose_name='Квартира')
    pr_doc_attorney = models.ImageField(
        upload_to=user_dir_path, max_length=100, verbose_name='Копия паспорта')
    pr_doc_ownership = models.ImageField(
        upload_to=user_dir_path, max_length=100, verbose_name='Документы, подтверждающие право собственности')
    pr_doc_family = models.ImageField(
        upload_to=user_dir_path, max_length=100, verbose_name='Справка о составе семьи')

    def __str__(self):
        self.ps_status = self.pr_Name
        return self.ps_status

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы на перегистрацию'
