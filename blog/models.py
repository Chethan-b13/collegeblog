from django.db import models
from django.contrib.auth.models import User

cat = (
    ('Events','Events'),
    ('Articles','Articles'),
    ('Art','Art'),
)

 

class Category(models.Model):
    category_names = models.CharField(max_length=200)


    def __str__(self):
        return self.category_names


    class Meta:
        verbose_name_plural = "Categories"    


class Posts(models.Model):
    status_choices = (
        ('Draft','Draft'),
        ('Publish','Publish'),
    )
    title = models.CharField(max_length=200, default='')
    post_image = models.ImageField(upload_to='media/pics', default='/static/images/campus.jpg')
    desc = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    is_hot = models.BooleanField(default= False, null= True, blank= True)
    status = models.CharField(max_length=20 , choices=status_choices, default='Draft')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Posts"    


