# Login/urls.py
from django.urls import path
from Login.views import *
app_name = 'Login'

urlpatterns = [
    path('userprofileinfo/', user_login),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]