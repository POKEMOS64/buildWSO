# Generated by Django 4.2.5 on 2023-10-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receipt',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic11_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №1-Доп поле'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic12_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №2-Доп поле'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic13_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №3-Доп поле'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic14_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №4-Доп поле'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic15_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №5-Доп поле'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='lic16_pole',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лицевой №6-Доп поле'),
        ),
    ]
