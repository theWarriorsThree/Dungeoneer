from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def is_in(var, obj):
    return var in obj