from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def fixRechargeTypes(value):
    if value == 'ATWILL':
        return 'At-Will'
    if value == 'ENCOUNTER':
        return 'Encounter'
    if value == 'DAILY':
        return 'Daily'