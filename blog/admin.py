from django.contrib import admin
from .models import Posts,Category,UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display= ('user','profile_pic','user_link')
    list_editable= ('profile_pic','user_link')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','likes','status','category','is_hot','post_image')
    prepopulated_fields = {'slug':('title',)}
    list_editable=('post_image','category','is_hot','likes')

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)
admin.site.register(UserInfo,UserInfoAdmin)
