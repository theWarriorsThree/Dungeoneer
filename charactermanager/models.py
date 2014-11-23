from django.db import models

# Create your models here.
class Character(models.Model):
	name = models.CharField(max_length=16)
	abilities = models.ManyToManyField("Ability")

	def __unicode__(self):
		return self.name

class Ability(models.Model):
	RECHARGE_CHOICES = (
		('ATWILL', 'At-Will'),
		('ENCOUNTER', 'Encounter'),
		('DAILY', 'Daily')
	)
	ACTION_TYPE_CHOICES = (
		('EMPTY','--'),
		('STANDARD','Standard action'),
		('MOVE','Move action'),
		('INTERRUPT','Immediate Interrupt'),
		('REACTION','Immediate reaction'),
		('MINOR','Minor Action'),
		('OPPORTUNTIY','Opportunity Action'),
		('FREE','Free Action'),
		('NONE','No Action')
	)

	ATTACK_TYPE_CHOICES = (
		('EMPTY','--'),
		('ME','Melee'),
		('MB','Melee Base'),
		('RA','Ranged'),
		('RB','Ranged Basic'),
		('MR','Melee or Ranged'),
		('CB','Close Burst'),
		('BL','Close Blast'),
		('AB','Area Burst'),
		('AW','Area Wall'),
		('AA','Area'),
		('PE','Personal')
	)

	ATTACK_STAT_CHOICES = (
		('EMPTY','--'),
		('STENGTH','Strength'),
		('CONSTITUTION','Constitution'),
		('DEXTERITY','Dexterity'),
		('INTELLIGENCE','Intelligence'),
		('CHARISMA','Charisma'),
		('WISDOM','Wisdom')
	)

	DEFENSE_STAT_CHOICES = (
		('EMPTY','--'),
		('AC','AC'),
		('FORTITUDE','Fortitude'),
		('REFLEX','Reflex'),
		('WILL','Will')
	)

	SUSTAIN_CHOICES = (
		('EMPTY','--'),
		('MINOR','Minor'),
		('MOVE','Move'),
		('STANDARD','Standard')
	)

	name = models.CharField(max_length=32)
	level = models.CharField(max_length=32)
	flavor = models.TextField()
	recharge = models.CharField(max_length=2,choices=RECHARGE_CHOICES, default='ATWILL')
	keywords = models.CharField(max_length=32)
	actionType = models.CharField(max_length=2,choices=ACTION_TYPE_CHOICES, default='EMPTY')
	attackType = models.CharField(max_length=2,choices=ATTACK_TYPE_CHOICES, default='EMPTY')
	attackRange = models.CharField(max_length=32)
	trigger = models.CharField(max_length=32)
	prerequisite = models.CharField(max_length=32)
	requirement = models.CharField(max_length=32)
	target = models.CharField(max_length=32)
	attackStat = models.CharField(max_length=2,choices=ATTACK_STAT_CHOICES, default='EMPTY')
	attackStatNote = models.CharField(max_length=32)
	defenseStat = models.CharField(max_length=2,choices=DEFENSE_STAT_CHOICES, default='EMPTY')
	defenseStatNote = models.CharField(max_length=32)
	hit = models.TextField()
	miss = models.TextField()
	secondaryTarget = models.CharField(max_length=32)
	secondaryAttack = models.CharField(max_length=32)
	effect = models.TextField()
	sustainType = models.CharField(max_length=2,choices=SUSTAIN_CHOICES, default='EMPTY')
	sustainNote = models.CharField(max_length=32)
	special = models.TextField()