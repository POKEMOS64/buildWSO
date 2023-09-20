# Generated by Django 4.2.5 on 2023-09-19 11:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dispatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAd', models.DateField(max_length=50, verbose_name='Дата')),
                ('gapTime', models.CharField(max_length=50, verbose_name='Промежуток времени')),
                ('optMaps', models.CharField(max_length=100, null=True, verbose_name='Улица или поселок с номером')),
                ('optMaps_one', models.CharField(max_length=100, null=True, verbose_name='Улица или поселок с номером')),
            ],
            options={
                'verbose_name': 'Событие ремонтных работ',
                'verbose_name_plural': 'Событие ремонтных работ',
            },
        ),
        migrations.CreateModel(
            name='dispatchText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='заголовок')),
                ('sectionText', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Содержимое страницы',
                'verbose_name_plural': 'Содержимое страниц',
            },
        ),
    ]