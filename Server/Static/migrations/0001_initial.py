# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero_Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leader_Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Hero_Ability')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Leader')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('file_path', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('shortname', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Terrain_Unit_Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move', models.FloatField(default=1.0)),
                ('terrain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Terrain')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0)),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Stat')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='unit_stat',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='terrain_unit_movement',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='terrain',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='stat',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='perk',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='map',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='leader_ability',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='leader',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='hero_ability',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='class',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AddField(
            model_name='action',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Static.Version'),
        ),
        migrations.AlterUniqueTogether(
            name='unit_stat',
            unique_together=set([('stat', 'unit', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='terrain_unit_movement',
            unique_together=set([('terrain', 'unit', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='terrain',
            unique_together=set([('shortname', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='stat',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='perk',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='map',
            unique_together=set([('file_path', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='leader_ability',
            unique_together=set([('leader', 'ability', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='leader',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='hero_ability',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='action',
            unique_together=set([('name', 'version')]),
        ),
    ]
