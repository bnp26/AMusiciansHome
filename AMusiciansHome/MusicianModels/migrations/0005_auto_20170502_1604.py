# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicianModels', '0004_auto_20170501_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]