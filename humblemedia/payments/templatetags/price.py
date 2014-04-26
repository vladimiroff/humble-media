from django import template

register = template.Library()


@register.filter
def price(amount):
    return '{:.2f} BGN'.format(amount / 100)
