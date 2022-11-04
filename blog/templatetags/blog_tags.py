# Simple tag processes the given data and returns a string

from django import template
from ..models import Post

register = template.Library()  #used to register the template tag
# Django will use the function name as the tag name

@register.simple_tag
def total_posts():
    return Post.published.count()  #it returns the number of post published in the blog