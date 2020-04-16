from django import forms
from django.contrib.auth.models import User
from blog.models import Posts
from django.contrib.auth.forms import UserCreationForm 

class SignUpForm(UserCreationForm):
    username = forms.CharField( max_length=25, widget=forms.TextInput( attrs={
                'style': 'border: 0px;',
                'placeholder': 'Username',
    }))
    email = forms.EmailField(max_length=200,

    widget=forms.EmailInput(attrs={
                'style': 'border: 0px;',
                'placeholder': 'Mail',
    })
    )
    
    Phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'style':'border:0px',
            'placeholder':'Phone Number'
        }
    ))

    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={
            'style':'border:0px',
            'placeholder':'Password'
        }
    ))

    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={
            'style':'border:0px',
            'placeholder':'Reapeat Password'
        }
    ))

    profile_pic = forms.FileField(label='Upload_your image' , help_text='Blank If you choose it to upload later', required=False)
    user_link = forms.URLField(label='Your Social link', required=False, help_text="Blank if you dont have one ")
    
    class Meta:
        model = User
        # fields = ('username','email','profile_pic','user_link',"password1",'password2')
        fields = ('username', 'email', 'password1', 'password2', 'Phone_number', 'profile_pic', 'user_link')


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'post_image', 'desc', 'category', 'post_link', 'status')


