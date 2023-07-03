from django import template

register = template.Library()

@register.filter
def fill_password(password):
    return "•" * len(password)
