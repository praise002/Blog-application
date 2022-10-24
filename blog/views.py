from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Post


def post_list(request):
    post_list = Post.published.all()
    #pagination with 3 post per page
    paginator = Paginator(post_list, 3)  #instantiate it with d no of objects to return per page
    page_number = request.GET.get('page', 1)  #we retrieve d page and store it in page_number variable
    try:
        posts = paginator.page(page_number)  #obtain result for desired page
    except PageNotAnInteger:
        #if page number is not an integer deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page number is out of range deliver last page of results: num pages is the same as last page number
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts': posts}
    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                            status=Post.Status.PUBLISHED, 
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)
