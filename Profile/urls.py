from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('<int:id>/<username>/', views.profile, name='profile'),
    path('delete/<int:id>/', views.Post_delete, name='PostDelete'),
]
