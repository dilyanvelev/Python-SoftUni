from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize_filter(value):
    """
    Capitalize the value i.e. makes the first letter capital
    and lowers the rest.
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()
