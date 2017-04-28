# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-28 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MusicianModels', '0008_auto_20170427_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instr',
            name='date_made',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='date_made',
        ),
        migrations.AddField(
            model_name='instr',
            name='year_made',
            field=models.IntegerField(default=2005),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supply',
            name='year_made',
            field=models.IntegerField(blank=True, default=2008),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='object',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 28, 18, 23, 50, 392058, tzinfo=utc)),
        ),
    ]
