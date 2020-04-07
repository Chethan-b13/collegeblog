from django.urls import path
from . import views

app_name = 'blog'

urlpatterns= [
    path('', views.Indexview.as_view(), name='home'),
    path('blog/<int:id>/<slug:slug>/',views.detailview,name='detail'),
]