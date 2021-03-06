# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatcherContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batcher_position', models.IntegerField()),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('division_name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Extruder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extruder_position', models.IntegerField(verbose_name='Extruder position')),
                ('extruder_name', models.CharField(max_length=50, verbose_name='Extruder name')),
                ('batchers_qty', models.IntegerField(verbose_name='Quantity of batchers')),
                ('incapsulation', models.BooleanField()),
                ('recycled', models.FloatField()),
                ('inlet_of_recycled', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtrusionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extrusion_type_name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('formula_name', models.CharField(max_length=200, unique=True)),
                ('productivity', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
                ('extruder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Extruder')),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('machine_name', models.CharField(max_length=200, unique=True)),
                ('incapsulation', models.BooleanField()),
                ('recycling', models.BooleanField()),
                ('description', models.TextField()),
                ('set_in', models.CharField(choices=[('mass', 'mass percentage'), ('thickness', 'thickness')], max_length=50)),
                ('settable_accuracy', models.FloatField(choices=[(1, '1'), (0.1, '0.1'), (0.01, '0.01'), (0.001, '0.001')])),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Division')),
                ('extrusion_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.ExtrusionType')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=200)),
                ('resin_name', models.CharField(max_length=200, unique=True)),
                ('material_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.MaterialType')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('structure_name', models.CharField(max_length=200, unique=True, verbose_name='Структура')),
            ],
        ),
        migrations.AddField(
            model_name='formula',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Machine'),
        ),
        migrations.AddField(
            model_name='formula',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Structure'),
        ),
        migrations.AddField(
            model_name='extruder',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Machine'),
        ),
        migrations.AddField(
            model_name='batchercontent',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturing.Layer'),
        ),
        migrations.AddField(
            model_name='batchercontent',
            name='resin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manufacturing.Resin'),
        ),
    ]
