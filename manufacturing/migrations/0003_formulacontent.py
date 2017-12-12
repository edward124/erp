# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0002_auto_20171123_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Formula')),
                ('resin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Resin')),
            ],
        ),
    ]
