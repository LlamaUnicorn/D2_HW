from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    """
   value: значение, к которому нужно применить фильтр
   """
    censored = ['новости']
    for value in censored:
        censored_word = '*' * len(value)
    return censored_word

    # Возвращаемое функцией значение подставится в шаблон.
