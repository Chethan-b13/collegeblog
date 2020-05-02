from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Posts, Comment, Category
from Accounts.forms import CommentForm

class Indexview(generic.ListView):
    template_name = 'blog/index.html'
    model = Posts
    def get_context_data(self, *, object_list=None, **kwargs):
        
        Hot_News = Posts.published.all().order_by('-id')
        Events = Hot_News.filter(category=1).annotate(l_count=Count('likes')).order_by('-l_count')
        Articles = Hot_News.filter(category=3).annotate(l_count=Count('likes')).order_by('-l_count')
        Art = Hot_News.filter(category=2).annotate(l_count=Count('likes')).order_by('-l_count')
        Top = Hot_News.annotate(l_count=Count('likes')).order_by('-l_count')

        return {'Hot_News':Hot_News, 'Top':Top, 'Articles':Articles, 'Art':Art, 
                'Top4_side':Hot_News[:4], 'side_Art':Art, 'Events':Events
                }




@login_required
def PostLike(request):
    post = get_object_or_404(Posts, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    # return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'is_liked':is_liked,
        'condtion':post,
    }
    if request.is_ajax():

        html = render_to_string('blog/like.html', context, request=request)
        return JsonResponse({'form': html})


def detailview(request, id, slug):
    Post = get_object_or_404(Posts, pk=id)
    comments = Comment.objects.filter(Post=Post, Reply=None).order_by('-id')
    News = Posts.published.all().order_by('-id')
    ManyPosts = News.filter(category=Post.category).annotate(l_count=Count('likes')).order_by('-l_count')[:4]
    Art = News.filter(category=2).annotate(l_count=Count('likes')).order_by('-l_count')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = comment_form.save(commit=False)
            reply_id = request.POST.get('comment_id')
            content.Reply = None
            if reply_id:
                content.Reply = Comment.objects.get(id=reply_id)
            content.user = User.objects.get(id=request.user.id)
            content.Post = Posts.objects.get(id=Post.id)
            content.save()
            comment_form = CommentForm()
            
    else:
        comment_form = CommentForm()

    context = {
        'Post':Post, 
        'Cat_posts':ManyPosts, 
        'Top4_side':News[:4], 
        'Comments':comments,
        'comment_form':comment_form,
        'Art':Art,        
    }

    if request.is_ajax():
        messages.success(request,"Comment Posted !")
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})


    return render(request, 'blog/detail.html', context)


@login_required
def CommentDelete(request, id):
    comment = get_object_or_404(Comment,id=id)
    post = comment.Post
    comment.delete()
    comments = Comment.objects.filter(Post=post.id, Reply=None).order_by('-id')
    context = {
        'Comments':comments,
        'comment_form' : CommentForm()
    }

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})


def Category_List(request, id, category):
    category_post = Posts.published.filter(category=id).order_by('-id')
    category = Category.objects.get(id=id)
    News = Posts.published.order_by('-id')
    Art = News.filter(category=2).annotate(l_count=Count('likes')).order_by('-l_count')
    return render(request, 'blog/category.html', {'Category_Posts':category_post, 'category':category,
                                                  'Top4_side':News[:4], 'Art':Art })
                                                            