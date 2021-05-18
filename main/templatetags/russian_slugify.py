from django import template
from pytils.translit import slugify, translify

register = template.Library()


@register.filter(name='russian_slugify')
def russian_slugify(value):
    """Returns translate of russian string to slug"""
    return slugify(value)
