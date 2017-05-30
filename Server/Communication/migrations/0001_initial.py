# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-21 17:56
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsyncMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('message_key', models.TextField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('sent', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.Users')),
            ],
        ),
    ]