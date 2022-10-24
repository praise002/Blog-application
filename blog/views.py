from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from . models import Post


def post_list(request):
    post_list = Post.published.all()
    #pagination with 3 post per page
    paginator = Paginator(post_list, 3)
    context = {'posts': posts}
    return render(request, 'blog/post/list.html', context)


# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         return Http404('No post found.')
#     context = {'post': post}
#     return render(request, 'blog/post/detail.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                            status=Post.Status.PUBLISHED, 
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)
