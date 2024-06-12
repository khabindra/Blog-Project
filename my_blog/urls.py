from django.urls import path
from .views import *



urlspatterns = [
    path('',landing_page,name='landing_page'),
    path('posts',posts,name='posts_page'),
    path('posts/<slug:slug>/',post_detail,name='detail_posts_page'),


]