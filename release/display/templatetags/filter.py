from django import template

register = template.Library()

@register.filter
def dic_value(dic, key):
    return dic[key]

print(type(register))
