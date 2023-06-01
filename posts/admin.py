from django.contrib import admin
from .models import Post, Comment, Category
import os
#configuraciones panel administrador

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'body', 'created', 'owner')

class AdminComment(admin.ModelAdmin):
    list_display = ('comment','created', 'owner')

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
# Register your models here.

admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
admin.site.register(Category, AdminCategory)

#admin.site.site_url = os.environ.get('FRONT_SITE_URL', default='http://127.0.0.1:5173')
