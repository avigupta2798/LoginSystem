# Create your models here.
# Login/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __user__(self):
        return "%s" % self.user.username
    
    def __str__(self):
        return "%s" % self.name