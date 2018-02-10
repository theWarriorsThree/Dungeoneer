from charactermanager.models import Monster
from charactermanager.models import Character
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.assignment_tag
def getMonsters(cat, subCat=None):
    monsters = None
    if(subCat == None):
        monsters = Monster.objects.filter(category=cat,subCategory__isnull=True)
    else:
        monsters = Monster.objects.filter(category=cat,subCategory=subCat)
    return monsters

@register.simple_tag
def addIntegerSign(num):
    if(num == ""):
        return ""
    if(num > 0):
        return "+" + str(num)
    else:
        return num