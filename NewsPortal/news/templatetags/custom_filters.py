from django import template

register = template.Library()


@register.filter()
def censor(value):
    profanity = ['соня', 'дом', 'редиска']
    for i in profanity:
        if i.find(value):
            value = value.replace(i[1::], "*" * (len(i)-1))
    return f'{value}'
