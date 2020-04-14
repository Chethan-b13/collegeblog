from django.shortcuts import render, redirect
from blog.models import UserInfo
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserCreationForm,PostCreationForm
from django.template.defaultfilters import slugify
from django.urls import reverse


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})

# Create your views here.
def Register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            prof_pic = form.cleaned_data.get('profile_pic')
            user_link = form.cleaned_data.get('user_link')

            userinfo = UserInfo.objects.create(user=user, profile_pic=prof_pic, user_link=user_link)
            userinfo.save()
            
            created_user = authenticate(username=username, password=password)
            login(request, created_user)

            return redirect('blog:home')
    else:
        form = SignUpForm() 

    return render(request, 'accounts/register.html', {'form':form})

# def Prof_creation(request,id):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST,request.FILES)  

#         if form.is_valid():
#             Info = form.save(commit=False)
#             UserInfo.user = id

def ConfirmRegister(request):
    return render(request, 'accounts/confirm.html')

def Logout(request):
    auth.logout(request)
    return redirect('blog:home')


@login_required(login_url="/accounts/login/")
def CreatePost(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            Post = form.save(commit=False)
            user= UserInfo.objects.get(user=request.user)
            Post.author = user
            Post.slug = slugify(Post.title)
            Post.save()

            return redirect(reverse('blog:detail', kwargs={'id':Post.id, 'slug':Post.slug}))

    else:
        form = PostCreationForm()

    return render(request, 'accounts/CreatePost.html', {'form':form})    