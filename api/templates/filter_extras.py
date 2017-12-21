from django import template
import numpy as np

register = template.Library()

@register.filter(name='get_branche')

def get_branche(body_list, branche):	
    return ((body_list[body_list.branche == branche]).body)

@register.filter(name='index')
def index(List, i):
    return List[int(i)]

@register.filter(name='enum')
def enum(List):
    return np.arange(0,len(List))

@register.filter(name='indexq')
def index(QuerySet, i):
    return QuerySet[int(i)]

@register.filter(name='enum_dict')
def enum_dict(Dict):
    return np.arange(1,len(Dict)+1)

@register.filter(name='get_item_dict')
def get_item_dict(Dict, int):
    return Dict[str(int)]

