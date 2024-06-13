from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.views import View
from .models import Post
from django.urls import reverse_lazy,reverse
from .forms import UserRegisterForm,CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.utils.text import slugify
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
    

class AllPostView(LoginRequiredMixin,ListView):
    template_name = 'my_blog/all_posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'



# class DetailPostView(LoginRequiredMixin,DetailView):
#     template_name = 'my_blog/post_detail.html'
#     model = Post

class DetailPostView(LoginRequiredMixin,View):
    template_name = 'my_blog/post_detail.html'  
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {'post': post,
                   'comment_form':CommentForm()
                   }
        return render(request, self.template_name, context)
    
    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post 
            comment.save()

            return HttpResponseRedirect(reverse('detail_post_page',args=[slug]))
        
        context = {
            'post':post,
            'comment_form':CommentForm()
        }
        return render(request,'my_blog/post_detail.html',context)


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



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'my_blog/create_post.html'
    fields = ['title','token','image','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.cleaned_data['title']) 
        return super().form_valid(form)
    success_url = reverse_lazy('posts_page')
    



class PostUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    template_name = 'my_blog/create_post.html'
    model = Post
    fields = ['title','token','image','content']
    success_url = reverse_lazy('posts_page')
    
    def form_valid(self, form):
        form.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts_page')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
