# Simple tag processes the given data and returns a string
# Inclusion tags processes the given data and returns a rendered template

from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from ..models import Post
import markdown

register = template.Library()  #used to register the template tag
# Django will use the function name as the tag name

@register.simple_tag
def total_posts():
    return Post.published.count()  #it returns the number of post published in the blog


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}  #it returns a dict of variables

@register.simple_tag
def get_most_commented_posts(count=5): #count is a default
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    
@register.filter(name='markdown')  #markdown will be used in templates
def markdown_format(text):
    return mark_safe(markdown.markdown(text))