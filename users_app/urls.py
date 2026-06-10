from django.urls import path
from .views import create_post, home

urlpatterns = [
    path('', home, name='home'),
    path('create-post/', create_post, name='create_post'),
]