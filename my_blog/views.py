from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
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

# Custom login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts_page')  # Use the redirect function here
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'my_blog/login.html', {'form': form})

# Custom logout view
def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing_page'))