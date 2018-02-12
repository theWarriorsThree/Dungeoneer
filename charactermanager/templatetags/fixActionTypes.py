from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def fixActionTypes(value):
    if value == 'STANDARD':
        return 'Standard Action'
    if value == 'MINOR':
        return 'Minor Action'
    if value == 'MOVE':
        return 'Move Action'
    if value == 'INTERRUPT':
        return 'Immediate Interrupt'
    if value == 'REACTION':
        return 'Immediate reaction'
    if value == 'OPPORTUNTIY':
        return 'Opportunity Action'
    if value == 'FREE':
        return 'Free Action'