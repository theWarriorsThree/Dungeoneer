from django.db import models
from autoslug import AutoSlugField
from multiselectfield import MultiSelectField

#General Choices

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

MONSTER_POWER_TYPE_CHOICES = (
    ('ME','Melee'),
    ('RA','Ranged'),
    ('CL','Close'),
    ('AR','Area'),
    ('MB','Melee Basic'),
    ('RB','Ranged Basic')
)

ROLE_CHOICES = (
    ('AR','Artillery'),
    ('BR','Brute'),
    ('CO','Controller'),
    ('LU','Lurker'),
    ('MI','Minion'),
    ('SK','Skirmisher'),
    ('SO','Soldier'),
    ('SL','Solo'),
    ('LE','Leader')
)

SIZE_CHOICES = (
    ('TI','Tiny'),
    ('SM','Small'),
    ('ME','Medium'),
    ('LA','Large'),
    ('HU','Huge'),
    ('GA','Gargantuan')
)

ALIGNMENT_CHOICES = (
    ('GO','Good'),
    ('LG','Lawful Good'),
    ('EV','Evil'),
    ('CE','Chaotic Evil'),
    ('UN','Unaligned')
)

LANGUAGE_CHOICES = (
    ('AB','Abyssal'),
    ('CO','Common'),
    ('DR','Draconic'),
    ('DW','Dwarven'),
    ('EL','Elven'),
    ('DS','Deep Speech'),
    ('GI','Giant'),
    ('GO','Goblin'),
    ('PR','Primordial'),
    ('SU','Supernal')
)

#Campaigns

class Campaign(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name', unique=True,editable=True)
    image = models.ImageField(upload_to='uploaded/campaigns/',blank=True,default='')
    color = models.CharField(max_length=7,default='#8F65A8')
    characters = models.ManyToManyField('Character',blank=True)

    def __unicode__(self):
        return self.name


#Characters

class Character(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name', unique=True,editable=True)
    image = models.ImageField(upload_to='uploaded/characters/',blank=True,default='')
    abilities = models.ManyToManyField('Ability',blank=True)
    summary = models.TextField(blank=True,default='')
    background = models.TextField(blank=True,default='')

    def __unicode__(self):
        return self.name

class Ability(models.Model):

    name = models.CharField(max_length=64,blank=True)
    level = models.CharField(max_length=64,blank=True)
    flavor = models.TextField(blank=True)
    recharge = models.CharField(max_length=64,choices=RECHARGE_CHOICES, default='ATWILL',blank=True)
    keywords = models.ManyToManyField('AbilityKeyword',blank=True)
    actionType = models.CharField(max_length=64,choices=ACTION_TYPE_CHOICES,blank=True)
    attackType = models.CharField(max_length=64,choices=ATTACK_TYPE_CHOICES,blank=True)
    attackRange = models.CharField(max_length=64,blank=True)
    trigger = models.TextField(blank=True)
    prerequisite = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    target = models.CharField(max_length=64,blank=True)
    attackStat = models.CharField(max_length=64,choices=ATTACK_STAT_CHOICES, default='EMPTY',blank=True)
    attackStatNote = models.CharField(max_length=128,blank=True)
    defenseStat = models.CharField(max_length=64,choices=DEFENSE_STAT_CHOICES, default='EMPTY',blank=True)
    defenseStatNote = models.CharField(max_length=128,blank=True)
    hit = models.TextField(blank=True)
    miss = models.TextField(blank=True)
    secondaryTarget = models.CharField(max_length=64,blank=True)
    secondaryAttack = models.CharField(max_length=64,blank=True)
    effect = models.TextField(blank=True)
    sustainType = models.CharField(max_length=64,choices=SUSTAIN_CHOICES, default='EMPTY',blank=True)
    sustainNote = models.CharField(max_length=128,blank=True)
    special = models.TextField(blank=True)
    notes = models.TextField(blank=True,default='')
    source = models.CharField(max_length=64,blank=True,default='')

    def __unicode__(self):
        return self.name
    
    
class AbilityKeyword(models.Model):
    name = models.CharField(max_length=16,unique=True)
    
    def __unicode__(self):
        return self.name


#MonsterManager

class MonsterSubCategory(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name

    def getMonsters(self,category):
        return Monster.objects.filter(category=category.id,subCategory=this.id)

class MonsterCategory(models.Model):
    name = models.CharField(max_length=64,unique=True) 
    subCategories = models.ManyToManyField('MonsterSubCategory',blank=True,related_name='subCategories')

    def __unicode__(self):
        return self.name
    
    def getMonsters(self):
        return Monster.objects.filter(category=this.id,subCategory__isnull=True)


class MonsterKeyword(models.Model):
    name = models.CharField(max_length=16,unique=True)
    
    def __unicode__(self):
        return self.name
    
class Monster(models.Model):
    category = models.ForeignKey(MonsterCategory,related_name='monsters')
    subCategory = models.ForeignKey(MonsterSubCategory,related_name='monsters',null=True,blank=True)
    name = models.CharField(max_length=64,unique=True)
    level = models.CharField(max_length=64,blank=True)
    role = models.CharField(max_length=64,choices=ROLE_CHOICES, default='EMPTY',blank=True)
    size = models.CharField(max_length=64,choices=SIZE_CHOICES, default='EMPTY',blank=True)
    origin = models.CharField(max_length=64,unique=True)
    monsterType = models.CharField(max_length=64,unique=True)
    keywords = models.ManyToManyField('MonsterKeyword',blank=True)
    XP = models.CharField(max_length=64,blank=True)
    initiative = models.IntegerField(max_length=64,null=True,blank=True)
    perception = models.IntegerField(max_length=64,null=True,blank=True)
    specialSenses = models.CharField(max_length=64,blank=True)
    aura = models.CharField(max_length=64,blank=True)
    auraKeywords = models.ManyToManyField('AbilityKeyword',blank=True)
    auraRange = models.IntegerField(max_length=64,null=True,blank=True)
    auraEffect = models.TextField(blank=True)
    HP = models.IntegerField(max_length=64,null=True,blank=True)
    bloodied = models.IntegerField(max_length=64,null=True,blank=True)
    AC = models.IntegerField(max_length=64,null=True,blank=True)
    fortitude = models.IntegerField(max_length=64,null=True,blank=True)
    reflex = models.IntegerField(max_length=64,null=True,blank=True)
    will = models.IntegerField(max_length=64,null=True,blank=True)
    savingThrow = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(max_length=64,null=True,blank=True)
    specialSpeed = models.CharField(max_length=64,null=True,blank=True)
    actionPoints = models.IntegerField(max_length=64,null=True,blank=True)

    alignment = models.CharField(max_length=64,choices=ALIGNMENT_CHOICES, default='EMPTY',blank=True)
    language = MultiSelectField(choices=LANGUAGE_CHOICES)

    languageNotes = models.TextField(blank=True)
    skills = models.CharField(max_length=64,blank=True)

    strScore = models.IntegerField(max_length=64,null=True,blank=True)
    strMod = models.IntegerField(max_length=64,null=True,blank=True)
    conScore = models.IntegerField(max_length=64,null=True,blank=True)
    conMod = models.IntegerField(max_length=64,null=True,blank=True)
    dexScore = models.IntegerField(max_length=64,null=True,blank=True)
    dexMod = models.IntegerField(max_length=64,null=True,blank=True)
    intScore = models.IntegerField(max_length=64,null=True,blank=True)
    intMod = models.IntegerField(max_length=64,null=True,blank=True)
    wisScore = models.IntegerField(max_length=64,null=True,blank=True)
    wisMod = models.IntegerField(max_length=64,null=True,blank=True)
    chaScore = models.IntegerField(max_length=64,null=True,blank=True)
    chaMod = models.IntegerField(max_length=64,null=True,blank=True)

    equipment = models.TextField(blank=True)
    inventory = models.TextField(blank=True)
    bookReference = models.CharField(max_length=64,blank=True)
    
    def __unicode__(self):
        return self.name

class MonsterPower(models.Model):
    powerType = models.CharField(max_length=64,choices=MONSTER_POWER_TYPE_CHOICES, default='EMPTY',blank=True)
    name = models.CharField(max_length=64,unique=True)
    actionType = models.CharField(max_length=64,choices=ACTION_TYPE_CHOICES,blank=True)
    sustain = models.TextField(blank=True)
    recharge = models.CharField(max_length=64,choices=RECHARGE_CHOICES, default='ATWILL',blank=True)
    rechargeDice = MultiSelectField(choices=( (1,1),(2,2),(3,3),(4,4),(5,5),(6,6) ), blank=True,null=True )
    keywords = models.ManyToManyField('AbilityKeyword',blank=True)
    powerEffect = models.TextField(blank=True)
    monster = models.ForeignKey(Monster,related_name='powers')
    
    def __unicode__(self):
        return self.name
