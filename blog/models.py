from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number = models.CharField(max_length=12, blank=True, default='')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='/profile_pics/def.jpg')
    user_link = models.URLField(max_length=200, blank=True)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural =  'UserInfos'   
 

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
                                    
    post_image = models.ImageField(upload_to='pics', default='/pics/campus.jpg')
    desc = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0, blank=True,null=True)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    post_link = models.URLField(max_length=200, null=True,blank=True)
    is_hot = models.BooleanField(default= False, null= True, blank= True)
    status = models.CharField(max_length=20, choices=status_choices, default='Draft')


    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'pk':self.pk, 'slug':self.slug})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Posts"    


