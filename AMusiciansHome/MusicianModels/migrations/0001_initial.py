# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 23:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('maker', models.CharField(max_length=30)),
                ('year_made', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pages', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('composer', models.CharField(max_length=30)),
                ('year_pub', models.IntegerField(blank=True, default=1905)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('est_price', models.IntegerField()),
                ('date_posted', models.DateField(auto_now=True)),
                ('post', models.BooleanField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=30)),
                ('year_made', models.IntegerField(blank=True)),
                ('description', models.CharField(max_length=120)),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicianModels.Object')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('tag_type', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='object',
            name='tags',
            field=models.ManyToManyField(blank=True, to='MusicianModels.Tag'),
        ),
        migrations.AddField(
            model_name='object',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='music',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicianModels.Object'),
        ),
        migrations.AddField(
            model_name='instr',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicianModels.Object'),
        ),
    ]
