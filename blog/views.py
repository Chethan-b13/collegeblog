from django.shortcuts import render , get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Posts



class Indexview(generic.ListView):
    # context_object_name = "News"
    template_name = 'blog/index.html'
    model = Posts
    def get_context_data(self, *, object_list=None, **kwargs):
        Hot_News = Posts.objects.all().order_by('-uploaded_date')[:5]
        Articles = Posts.objects.filter(category=3).order_by('-likes')
        Art = Posts.objects.filter(category=2).order_by('-uploaded_date')
        Top_news = Posts.objects.all().order_by('-likes')
        Top4_side = Posts.objects.all().order_by('-likes')[:4]
        return {'Hot_News':Hot_News, 'Top':Top_news, 'Articles':Articles, 'Art':Art, 'Top4_side':Top4_side}    

@login_required
def PostLike(request):
    post = get_object_or_404(Posts, id=request.POST.get('Post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return redirect('/')


def detailview(request, id, slug):
    Post = get_object_or_404(Posts, pk=id)
    Top4_side = Posts.objects.all().order_by('-likes')[:4]

    ManyPosts = Posts.objects.filter(category=Post.category).order_by('-likes')[:4]
    return render(request,'blog/detail.html',{'Post':Post,'Cat_posts':ManyPosts,'Top4_side':Top4_side})
