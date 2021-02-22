# Login/admin.py

from django.contrib import admin
from Login.models import UserProfileInfo, User
# Register your models here.

class UserProfileInfoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'email']
    list_display = ('id', 'name', 'phone', 'email') 

admin.site.register(UserProfileInfo, UserProfileInfoAdmin)