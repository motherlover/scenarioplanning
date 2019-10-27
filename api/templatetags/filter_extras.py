# Not sure whether this or the one in templates is used for calling from the js functions
from django import template
import numpy as np

register = template.Library()

@register.filter(name='get_branche')
def get_branche(body_list, branche):
    return (body_list[body_list.branche == branche])
