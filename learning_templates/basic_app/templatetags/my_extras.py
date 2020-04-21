from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out the values of "arg" from the string abs
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
