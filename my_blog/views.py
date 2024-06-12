from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.


class LandingPageView(ListView):
    template_name = 'my_blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:2]
        return data
    

def posts(request):
   pass


class DetailPostView(DetailView):
    template_name = 'my_blog/post_detail.html'
    model = Post
    
    pass


def Contactview(request):
    return render(request,'my_blog/contact.html') 
