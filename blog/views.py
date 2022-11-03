from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from . models import Post, Comment
from . forms import EmailPostForm, CommentForm


class PostListView(ListView):
    """Alternative post list view"""
    queryset = Post.published.all()
    context_object_name = 'posts' #the default is object_list e.g post_list
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
    
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
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
        }
    return render(request, 'blog/post/detail.html', context)


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(data=request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data  #a dict of form fields and their values
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read " \
                        f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'praizthecoder@gmail.com', [cd['to']])
            sent = True
            
    else:
        form = EmailPostForm()
            
    context = {'post': post,
            'form': form,
            'sent': sent}
    return render(request, 'blog/post/share.html', context)


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None 
    #A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a comment object without sending it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
        
    context = {
        'post': post, 
        'form': form, 
        'comment': comment
    }
    return render(request, 'blog/post/comment.html', context)