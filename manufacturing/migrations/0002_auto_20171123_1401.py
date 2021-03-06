# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batchercontent',
            options={'verbose_name': 'Вміст дозатору', 'verbose_name_plural': 'Вмісти дозаторів'},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'verbose_name': 'Дільниця', 'verbose_name_plural': 'Дільниці'},
        ),
        migrations.AlterModelOptions(
            name='extruder',
            options={'verbose_name': 'Екструдер', 'verbose_name_plural': 'Екструдери'},
        ),
        migrations.AlterModelOptions(
            name='extrusiontype',
            options={'verbose_name': 'Тип екструзії', 'verbose_name_plural': 'Типи екструзії'},
        ),
        migrations.AlterModelOptions(
            name='formula',
            options={'verbose_name': 'Рецептура', 'verbose_name_plural': 'Рецептури'},
        ),
        migrations.AlterModelOptions(
            name='layer',
            options={'verbose_name': 'Шар', 'verbose_name_plural': 'Шари'},
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машини'},
        ),
        migrations.AlterModelOptions(
            name='materialtype',
            options={'verbose_name': 'Тип матеріалу', 'verbose_name_plural': 'Типи матеріалів'},
        ),
        migrations.AlterModelOptions(
            name='resin',
            options={'verbose_name': 'Полімер', 'verbose_name_plural': 'Полімери'},
        ),
        migrations.AlterModelOptions(
            name='structure',
            options={'verbose_name': 'Структура', 'verbose_name_plural': 'Структури'},
        ),
        migrations.AlterField(
            model_name='batchercontent',
            name='percentage',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='batchercontent',
            name='resin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Resin'),
        ),
    ]
