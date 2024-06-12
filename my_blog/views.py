from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import UserRegisterForm

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
    

class AllPostView(ListView):
    template_name = 'my_blog/all_posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'




class DetailPostView(DetailView):
    template_name = 'my_blog/post_detail.html'
    model = Post


def Contactview(request):
    return render(request,'my_blog/contact.html') 

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'my_blog/register.html'