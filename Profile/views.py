from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Posts, UserInfo
from django.contrib.auth.admin import User
from django.contrib import messages

# from django.views.generic import DeleteView


# Create your views here.
@login_required
def profile(request, id, username):
    user = UserInfo.objects.get_or_create(user=User.objects.get(pk=id))
    Cat_posts = Posts.objects.filter(author=user[0])
    Top4_side = Posts.published.all().order_by('-likes')[:4]
    return render(request, 'profile/profile.html', {'USER':user[0], 'Cat_posts':Cat_posts, 'Top4_side':Top4_side})


def Post_delete(request, id):
    Post = Posts.objects.get(pk=id)
    user_id = Post.author.user.id
    username = Post.author
    Post.delete()
    messages.warning(request, "Post delted succesfully")
    return redirect('Profile:profile', id=user_id, username=username)