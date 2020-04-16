from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("Register/", views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('confirmation/', views.ConfirmRegister, name='confirm'),
    path('logout/', views.Logout, name='logout'),
    path('activate/<uidb64>/<token>', views.ActivateAccount.as_view(), name='activate'),
    path('CreatePost/', views.CreatePost, name='CreatePost')
]