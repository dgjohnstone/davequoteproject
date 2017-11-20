# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20171120_1836'),
        ('quotes_app', '0005_auto_20171120_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorite',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorite',
            field=models.ManyToManyField(related_name='favorites', to='login_app.User'),
        ),
    ]