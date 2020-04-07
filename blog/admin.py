from django.contrib import admin
from .models import Posts,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','category','is_hot','post_image')
    prepopulated_fields = {'slug':('title',)}
    list_editable=('post_image','category','is_hot')

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)