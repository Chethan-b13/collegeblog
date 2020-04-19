from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Posts, UserInfo
# from django.views.generic import DeleteView


# Create your views here.
@login_required
def profile(request, id, username):
    user = get_object_or_404(UserInfo, user__pk=id)
    Cat_posts = Posts.objects.filter(author=user.id)
    Top4_side = Posts.objects.all().order_by('-likes')[:4]
    return render(request, 'profile/profile.html', {'USER':user, 'Cat_posts':Cat_posts, 'Top4_side':Top4_side})


def Post_delete(request, id):
    Post = Posts.objects.get(pk=id)
    user_id = Post.author.user.id
    username = Post.author
    Post.delete()
    return redirect('Profile:profile', id=user_id, username=username)