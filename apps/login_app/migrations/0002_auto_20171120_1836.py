# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='dob',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
