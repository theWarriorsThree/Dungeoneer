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

class MonsterCategory(models.Model):
    name = models.CharField(max_length=64,unique=True) 
    subCategories = models.ManyToManyField('MonsterSubcategory',blank=True)

    def __unicode__(self):
        return self.name
    
class MonsterKeyword(models.Model):
    name = models.CharField(max_length=16,unique=True)
    
    def __unicode__(self):
        return self.name
    
class Monster(models.Model):
    name = models.CharField(max_length=64,unique=True)
    level = models.CharField(max_length=64,blank=True)
    role = models.CharField(max_length=64,choices=ROLE_CHOICES, default='EMPTY',blank=True)
    size = models.CharField(max_length=64,choices=SIZE_CHOICES, default='EMPTY',blank=True)
    origin = models.CharField(max_length=64,unique=True)
    monsterType = models.CharField(max_length=64,unique=True)
    keywords = models.ManyToManyField('MonsterKeyword',blank=True)
    initiative = models.CharField(max_length=64,blank=True)
    perception = models.CharField(max_length=64,blank=True)
    specialSenses = models.CharField(max_length=64,blank=True)
    aura = models.CharField(max_length=64,blank=True)
    auraKeywords = models.ManyToManyField('AbilityKeyword',blank=True)
    auraRange = models.CharField(max_length=64,blank=True)
    auraEffect = models.TextField(blank=True)
    HP = models.CharField(max_length=64,blank=True)
    bloodied = models.CharField(max_length=64,blank=True)
    AC = models.CharField(max_length=64,blank=True)
    fortitude = models.CharField(max_length=64,blank=True)
    reflex = models.CharField(max_length=64,blank=True)
    will = models.CharField(max_length=64,blank=True)
    savingThrow = models.TextField(blank=True)
    speed = models.CharField(max_length=64,blank=True)
    actionPoints = models.CharField(max_length=64,blank=True)

    alignment = models.CharField(max_length=64,choices=ALIGNMENT_CHOICES, default='EMPTY',blank=True)
    language = MultiSelectField(choices=LANGUAGE_CHOICES)

    languageNotes = models.TextField(blank=True)
    skills = models.CharField(max_length=64,blank=True)

    strScore = models.CharField(max_length=64,blank=True)
    strMod = models.CharField(max_length=64,blank=True)
    conScore = models.CharField(max_length=64,blank=True)
    conMod = models.CharField(max_length=64,blank=True)
    dexScore = models.CharField(max_length=64,blank=True)
    dexMod = models.CharField(max_length=64,blank=True)
    intScore = models.CharField(max_length=64,blank=True)
    intMod = models.CharField(max_length=64,blank=True)
    wisScore = models.CharField(max_length=64,blank=True)
    wisMod = models.CharField(max_length=64,blank=True)
    chaScore = models.CharField(max_length=64,blank=True)
    chaMod = models.CharField(max_length=64,blank=True)

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
    keywords = models.ManyToManyField('AbilityKeyword',blank=True)
    powerEffect = models.TextField(blank=True)
    monster = models.ForeignKey(Monster)
    
    def __unicode__(self):
        return self.name