from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Posts, Comment
from Accounts.forms import CommentForm


class Indexview(generic.ListView):
    template_name = 'blog/index.html'
    model = Posts
    def get_context_data(self, *, object_list=None, **kwargs):
        Hot_News = Posts.published.all().order_by('-id')
        Articles = Posts.published.filter(category=3).annotate(l_count=Count('likes')).order_by('-l_count')
        Art = Posts.published.filter(category=2).order_by('-uploaded_date')
        Top_news = Posts.published.annotate(l_count=Count('likes')).order_by('-l_count')
        Top4_side = Posts.published.annotate(l_count=Count('likes')).order_by('-l_count')[:4]
        return {'Hot_News':Hot_News, 'Top':Top_news, 'Articles':Articles, 'Art':Art, 'Top4_side':Top4_side}

    # def post(self, request, *args, **kwargs):
    #     post = get_object_or_404(Posts, id=request.POST.get('id'))
    #     is_liked = False
    #     if post.likes.filter(id=request.user.id).exists():
    #         is_liked = True
        
    #     return self.get_context_data()+{'is_liked':is_liked}


@login_required
def PostLike(request):
    post = get_object_or_404(Posts, id=request.POST.get('id'))
    print(post)
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
        print(context)
        html = render_to_string('blog/like.html', context, request=request)
        return JsonResponse({'form': html})


def detailview(request, id, slug):
    Post = get_object_or_404(Posts, pk=id)
    comments = Comment.objects.filter(Post=Post, Reply=None).order_by('-id')
    Top4_side = Posts.published.all().order_by('-likes')[:4]
    ManyPosts = Posts.published.filter(category=Post.category).order_by('-likes')[:4]

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
    else:
        comment_form = CommentForm()

    context = {
        'Post':Post, 
        'Cat_posts':ManyPosts, 
        'Top4_side':Top4_side, 
        'Comments':comments,
        'comment_form':comment_form
    }

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})


    return render(request, 'blog/detail.html', context)
