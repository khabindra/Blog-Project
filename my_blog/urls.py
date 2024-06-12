from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('posts', AllPostView.as_view(), name='posts_page'),
    path('posts/<slug:slug>/', DetailPostView.as_view(), name='detail_posts_page'),
    path('contact/',Contactview,name='contact_page'),
    path('signup/',SignUpView.as_view(),name='sign_up')
]
