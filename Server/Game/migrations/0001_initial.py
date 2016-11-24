# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Static', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_round', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_move', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('map_path', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Map')),
                ('user_turn', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.Users')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version')),
            ],
        ),
        migrations.CreateModel(
            name='Game_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.IntegerField(default=0)),
                ('victorious', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Game.Game')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Leader')),
                ('perk_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='perk_1', to='Static.Perk')),
                ('perk_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='perk_2', to='Static.Perk')),
                ('perk_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='perk_3', to='Static.Perk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp_remaining', models.IntegerField(default=0)),
                ('prev_hp', models.IntegerField(default=0)),
                ('x_pos', models.IntegerField(default=-1)),
                ('y_pos', models.IntegerField(default=-1)),
                ('prev_x', models.IntegerField(default=0)),
                ('prev_y', models.IntegerField(default=0)),
                ('game', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Game.Game')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.Users')),
                ('prev_action', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Action')),
                ('prev_target', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Game.Unit')),
                ('unit_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Class')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version')),
            ],
        ),
    ]
