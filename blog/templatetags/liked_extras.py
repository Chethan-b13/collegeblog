from django import template
from blog.models import Comment

register = template.Library()

@register.filter(name='Comment_count')
def liked(value):
    comments = Comment.objects.filter(Post=value)
    return comments.count()