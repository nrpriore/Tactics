from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
	game_round   = models.IntegerField(default=0)
	user_turn    = models.ForeignKey('User.Users',    on_delete=models.DO_NOTHING) 
	map_path     = models.ForeignKey('Static.Map',    on_delete=models.DO_NOTHING)
	created      = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_move    = models.DateTimeField(auto_now=True,  auto_now_add=False)
	finished     = models.BooleanField(default=False)
	version      = models.ForeignKey('Static.Version',on_delete=models.DO_NOTHING)
	

class Game_User(models.Model):
	game         = models.ForeignKey(Game,   		  on_delete=models.DO_NOTHING)
	user         = models.ForeignKey('User.Users',    on_delete=models.DO_NOTHING)
	team         = models.IntegerField(default=0)
	leader       = models.ForeignKey('Static.Leader', on_delete=models.DO_NOTHING)
	perk_1       = models.ForeignKey('Static.Perk',   on_delete=models.DO_NOTHING, null=True, related_name='perk_1')
	perk_2       = models.ForeignKey('Static.Perk',   on_delete=models.DO_NOTHING, null=True, related_name='perk_2')
	perk_3       = models.ForeignKey('Static.Perk',   on_delete=models.DO_NOTHING, null=True, related_name='perk_3')
	victorious   = models.BooleanField(default=False)

class Unit(models.Model):
	unit_class   = models.ForeignKey('Static.Class',  on_delete=models.DO_NOTHING)
	hp_remaining = models.IntegerField(default=0)
	prev_hp      = models.IntegerField(default=0)
	x_pos        = models.IntegerField(default=-1)
	y_pos        = models.IntegerField(default=-1)
	prev_x       = models.IntegerField(default=0)
	prev_y       = models.IntegerField(default=0)
	prev_target  = models.ForeignKey('self',          on_delete=models.DO_NOTHING, null=True, default=None)
	prev_action  = models.ForeignKey('Static.Action', on_delete=models.DO_NOTHING, null=True, default=None)
	owner        = models.ForeignKey('User.Users',    on_delete=models.DO_NOTHING)
	game         = models.ForeignKey('Game',          on_delete=models.DO_NOTHING, null=True, default=None)
	version      = models.ForeignKey('Static.Version',on_delete=models.DO_NOTHING)
