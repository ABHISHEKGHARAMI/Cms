# template tags for the views

from django import template

register = template.Library()


@register.filter
def model_name(self,obj):
    try:
        return obj.__meta.model_name
    except AttributeError:
        return None