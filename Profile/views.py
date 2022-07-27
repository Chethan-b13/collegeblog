from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from blog.models import Posts, UserInfo
from django.contrib.auth.admin import User
from django.contrib import messages
from Accounts.forms import ProfileForm, AdminUserForm


# Create your views here.
@login_required
def profile(request, id, username):
    user = get_object_or_404(UserInfo, user=User.objects.get(pk=id))
    if request.user.id == id:
        Cat_posts = Posts.objects.filter(author=user)
    else:
        Cat_posts = Posts.published.filter(author=user)
    Top4_side = Posts.published.all().order_by('-likes')[:4]
    return render(request, 'profile/profile.html', {'USER': user, 'Cat_posts': Cat_posts, 'Top4_side': Top4_side})


def Post_delete(request, id):
    Post = Posts.objects.get(pk=id)
    user_id = Post.author.user.id
    username = Post.author
    Post.delete()
    messages.warning(request, "Post deleted succesfully")
    return redirect('Profile:profile', id=user_id, username=username)


@login_required
def Edit_Profile(request):
    user = UserInfo.objects.get(user=request.user.id)
    if request.method == 'POST':
        UserInfoForm = ProfileForm(request.POST, request.FILES, instance=user)
        UserForm = AdminUserForm(request.POST, instance=request.user)

        if UserForm.is_valid() and UserInfoForm.is_valid():

            UserForm.save()
            UserInfoForm.save()
            messages.success(request, "Profile Edited Succesfully")
            return redirect(reverse('Profile:profile', kwargs={'id': request.user.id, 'username': request.user.username}))
    else:
        UserInfoForm = ProfileForm(instance=user)
        UserForm = AdminUserForm(instance=request.user)

    return render(request, 'profile/EditProfile.html', {'UserInfoForm': UserInfoForm, 'UserForm': UserForm})
