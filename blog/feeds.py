import markdown  
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy 
from . models import Post 


class LatestPostsFeeds(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')   
    description = 'New posts of my blog'