# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case1', '0003_delete_rang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangdate',
            name='date_end',
            field=models.DateField(blank=True, default='2017-04-17', verbose_name='дата окончания  встречи'),
        ),
        migrations.AlterField(
            model_name='rangdate',
            name='date_start',
            field=models.DateField(blank=True, default='2017-04-07', verbose_name='дата начала встречи'),
        ),
        migrations.AlterField(
            model_name='rangdate',
            name='time_end',
            field=models.IntegerField(default=18, verbose_name='время окончания  встречи'),
        ),
        migrations.AlterField(
            model_name='rangdate',
            name='time_start',
            field=models.IntegerField(default=9, verbose_name='время начала  встречи'),
        ),
    ]
