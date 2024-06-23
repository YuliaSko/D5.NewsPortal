from django import template

register = template.Library()

censor_words = ['lol', 'bad']


@register.filter()
def censor(value):
    for word in censor_words:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value
