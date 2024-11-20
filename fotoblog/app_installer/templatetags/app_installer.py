from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.filter
def app_url(app_name):
    try:
        reverse_url = reverse(f'{app_name}:{app_name}')

        return reverse_url

    except NoReverseMatch:
        return reverse(f'app_installer:default_home', args=[app_name])