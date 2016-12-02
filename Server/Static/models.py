from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Version(models.Model):
	name         = models.CharField(max_length=16, unique=True)
	price_max    = models.IntegerField(default=1000)
	unit_count   = models.IntegerField(default=8)
	
class Action(models.Model):	
	name         = models.CharField(max_length=16)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)
	description  = models.CharField(max_length=100)

	class Meta:
		unique_together = ('name', 'version')

class Class(models.Model):	
	name         = models.CharField(max_length=16)
	description  = models.CharField(max_length=100)
	price        = models.IntegerField(default=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('name', 'version')

class Hero_Ability(models.Model):
	name         = models.CharField(max_length=16)
	description  = models.CharField(max_length=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('name', 'version')

class Leader(models.Model):	
	name         = models.CharField(max_length=16)
	description  = models.CharField(max_length=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('name', 'version')

class Leader_Ability(models.Model):
	leader 		 = models.ForeignKey(Leader,       on_delete=models.DO_NOTHING)
	ability      = models.ForeignKey(Hero_Ability, on_delete=models.DO_NOTHING)
	version 	 = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('leader', 'ability', 'version')

class Perk(models.Model):
	name         = models.CharField(max_length=16)
	description  = models.CharField(max_length=100)
	tier         = models.IntegerField(default=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('name', 'version')

class Map(models.Model):
	name         = models.CharField(max_length=16)	
	file_path    = models.CharField(max_length=128)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('file_path', 'version')

class Stat(models.Model):
	name         = models.CharField(max_length=16)   # HP, Strength, Agility
	description  = models.CharField(max_length=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('name', 'version')

class Unit_Stat(models.Model):
	stat 		 = models.ForeignKey(Stat,		   on_delete=models.DO_NOTHING)
	unit         = models.ForeignKey(Class,        on_delete=models.DO_NOTHING)
	value        = models.FloatField(default=0)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('stat', 'unit', 'version')

class Terrain(models.Model):
	name		 = models.CharField(max_length=16)	# Mountain, Grass, Road
	shortname    = models.CharField(max_length=8)
	description  = models.CharField(max_length=100)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('shortname', 'version')

class Terrain_Unit_Movement(models.Model):
	terrain 	 = models.ForeignKey(Terrain,	   on_delete=models.DO_NOTHING)
	unit         = models.ForeignKey(Class,        on_delete=models.DO_NOTHING)
	move         = models.FloatField(default=1.0)
	version      = models.ForeignKey(Version,      on_delete=models.DO_NOTHING)

	class Meta:
		unique_together = ('terrain', 'unit', 'version')

