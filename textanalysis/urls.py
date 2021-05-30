from django.urls import path
from textanalysis.views import index_analysis

urlpatterns = [
    path('frequency/', index_analysis, name='index_analysis'),
]
