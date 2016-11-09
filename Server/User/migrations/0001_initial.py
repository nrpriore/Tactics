# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=1)),
                ('experience', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('pref_grid', models.IntegerField(default=100)),
            ],
        ),
    ]
