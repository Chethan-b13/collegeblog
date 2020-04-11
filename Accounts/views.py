from django.shortcuts import render, redirect
from blog.models import UserInfo
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserCreationForm


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
