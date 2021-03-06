# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing', '0003_formulacontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='resin',
            name='density',
            field=models.FloatField(default=0.9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='layer',
            name='extruder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Extruder'),
        ),
    ]
