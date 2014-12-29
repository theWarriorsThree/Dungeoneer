from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Campaign(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='uploaded/campaigns/',blank=True,default='')
    color = models.CharField(max_length=7,default='#8F65A8')
    characters = models.ManyToManyField('Character')

    def __unicode__(self):
        return self.name
    

class Character(models.Model):
    name = models.CharField(max_length=16)
    slug = AutoSlugField(populate_from='name', unique=True)
    abilities = models.ManyToManyField('Ability')
    summary = models.TextField(blank=True,default='')
    background = models.TextField(blank=True,default='')

    def __unicode__(self):
        return self.name

class Ability(models.Model):

    RECHARGE_CHOICES = (
        ('ATWILL', 'At-Will'),
        ('ENCOUNTER', 'Encounter'),
        ('DAILY', 'Daily')
    )
    ACTION_TYPE_CHOICES = (
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
        ('STENGTH','Strength'),
        ('CONSTITUTION','Constitution'),
        ('DEXTERITY','Dexterity'),
        ('INTELLIGENCE','Intelligence'),
        ('CHARISMA','Charisma'),
        ('WISDOM','Wisdom')
    )

    DEFENSE_STAT_CHOICES = (
        ('AC','AC'),
        ('FORTITUDE','Fortitude'),
        ('REFLEX','Reflex'),
        ('WILL','Will')
    )

    SUSTAIN_CHOICES = (
        ('MINOR','Minor'),
        ('MOVE','Move'),
        ('STANDARD','Standard')
    )

    name = models.CharField(max_length=32,blank=True)
    level = models.CharField(max_length=32,blank=True)
    flavor = models.TextField(blank=True)
    recharge = models.CharField(max_length=32,choices=RECHARGE_CHOICES, default='ATWILL',blank=True)
    keywords = models.ManyToManyField('AbilityKeyword')
    actionType = models.CharField(max_length=32,choices=ACTION_TYPE_CHOICES,blank=True)
    attackType = models.CharField(max_length=32,choices=ATTACK_TYPE_CHOICES,blank=True)
    attackRange = models.CharField(max_length=32,blank=True)
    trigger = models.TextField(blank=True)
    prerequisite = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    target = models.CharField(max_length=32,blank=True)
    attackStat = models.CharField(max_length=32,choices=ATTACK_STAT_CHOICES, default='EMPTY',blank=True)
    attackStatNote = models.CharField(max_length=32,blank=True)
    defenseStat = models.CharField(max_length=32,choices=DEFENSE_STAT_CHOICES, default='EMPTY',blank=True)
    defenseStatNote = models.CharField(max_length=32,blank=True)
    hit = models.TextField(blank=True)
    miss = models.TextField(blank=True)
    secondaryTarget = models.CharField(max_length=32,blank=True)
    secondaryAttack = models.CharField(max_length=32,blank=True)
    effect = models.TextField(blank=True)
    sustainType = models.CharField(max_length=32,choices=SUSTAIN_CHOICES, default='EMPTY',blank=True)
    sustainNote = models.CharField(max_length=32,blank=True)
    special = models.TextField(blank=True)
    notes = models.TextField(blank=True,default='')
    source = models.CharField(max_length=32,blank=True,default='')

    def __unicode__(self):
        return self.name
    
    
class AbilityKeyword(models.Model):
    name = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.name