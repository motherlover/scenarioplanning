## Python functions to be called from javascript files
from django import template
import numpy as np

register = template.Library()

@register.filter(name='get_branche')
def get_branche(body_list, branche):	
    return ((body_list[body_list.branche == branche]).body)


