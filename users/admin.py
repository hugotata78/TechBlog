from django.contrib import admin
from . models import User
import os

#configuraciones adminUser

class adminUser(admin.ModelAdmin):
    list_display =('username', 'email','first_name','last_name')

# Register your models here.
admin.site.register(User, adminUser)

#admin.site.site_url = os.environ.get('FRONT_SITE_URL', default='http://127.0.0.1:5173')
