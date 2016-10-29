# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=1)),
                ('experience', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField()),
                ('pref_grid', models.IntegerField(default=100)),
            ],
        ),
    ]
