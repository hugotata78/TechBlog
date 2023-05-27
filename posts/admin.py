from django.contrib import admin
from .models import Post, Comment, Category
import os

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

admin.site.site_url = os.environ.get('FRONT_SITE_URL', default='http://127.0.0.1:5173')
