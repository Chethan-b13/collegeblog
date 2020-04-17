from django.views import View
from django.contrib.auth.models import auth , User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from .utils import generate_token
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from blog.models import UserInfo
from django.template.defaultfilters import slugify
from django.urls import reverse
from .forms import SignUpForm, PostCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('blog:home')
            else:
                messages.info(request, 'Confirm Email')
                return redirect('accounts:login')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


# Create your views here.
def Register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()

            current_site  = get_current_site(request)
            subject  = 'Email confirmation by Collegeblog'
            message = render_to_string('accounts/activation.html', {
                'user': user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)
            })

            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
            # user.email_user(subject, message)
            # prof_pic = form.cleaned_data.get('profile_pic')
            # user_link = form.cleaned_data.get('user_link')
            user_num = form.cleaned_data.get('Phone_number')


            userinfo = UserInfo.objects.create(user=user, user_number=user_num)
            userinfo.save()
            messages.info(request, 'A mail has been sent to Your registered email.\n Make sure you confirm your email by clicking the link')
            return redirect('accounts:confirm')
            # if user.is_active:
            #     created_user = authenticate(username=username, password=password)
            #     login(request, created_user)
            #     return redirect('blog:home')
            # else:
            #     messages.info(request, 'A mail has been sent to Your registered email.\n Make sure you confirm your email by clicking the link')
    else:
        form = SignUpForm() 

    return render(request, 'accounts/register.html', {'form':form})

class ActivateAccount(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            # print(user.password)

        except Exception as exception:
            user=None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            print(user.is_active)
            messages.success(request, 'Account activated succesfully')
            # login(request,user)
            return redirect('accounts:confirm')
        return render(request, 'accounts/activateFailed.html', status=401)

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