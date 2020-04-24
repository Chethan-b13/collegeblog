from django.contrib import admin
from .models import Posts, Category, UserInfo, Comment

class UserInfoAdmin(admin.ModelAdmin):
    list_display= ('user','profile_pic','user_link')
    list_editable= ('profile_pic','user_link')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','category','is_hot','post_image')
    prepopulated_fields = {'slug':('title',)}
    list_editable=('post_image','category','status')
    list_filter=('author','category','uploaded_date',)

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(UserInfo,UserInfoAdmin)
