from django import template

register = template.Library()

@register.filter(name='liked')
def liked(value, arg):
    is_liked = False
    if value.likes.filter(id=arg).exists():
        is_liked = True
    return is_liked
