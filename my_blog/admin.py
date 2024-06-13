from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','date',)
    list_display = ('title','date','author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_email','text','post']
admin.site.register(Comment,CommentAdmin)
