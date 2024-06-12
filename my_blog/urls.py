from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('posts', posts, name='posts_page'),
    path('posts/<slug:slug>/', post_detail, name='detail_posts_page'),
    path('contact/',Contactview,name='contact_page'),
]
