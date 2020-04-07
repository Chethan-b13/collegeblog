from django.shortcuts import render 
from django.views import generic
from .models import Posts


# Create your views here.
class Indexview(generic.ListView):
    # context_object_name = "News"
    template_name = 'blog/index.html'
    model = Posts
    def get_context_data(self, *, object_list=None, **kwargs):
        News = Posts.objects.all()
        count = 0
        Articles = Posts.objects.filter(category=3).order_by('-likes')
        Art = Posts.objects.filter(category=2).order_by('-uploaded_date')
        Top_news = Posts.objects.all().order_by('-likes')[0]
        Top4_side = Posts.objects.all().order_by('-likes')[:4]
        
        return {'News':News, 'Top':Top_news,'Articles':Articles,'Art':Art,'Top4_side':Top4_side}    

# def home(request):
#     News = Posts.objects.all
#     Top = Posts.objects.get(pk=1)
#     for top in Posts.objects.all():
#         if top.likes > Top.likes:
#             Top=top
#     return render(request,'blog/index.html',{'News':News,'Top':Top})

def detailview(request,id,slug):
    Post = Posts.objects.get(id=id)
    return render(request,'blog/detail.html',{'Post':Post})