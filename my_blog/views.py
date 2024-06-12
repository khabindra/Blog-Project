from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,'my_blog/index.html')
def posts(request):
   pass


def post_detail(request):
    pass

def Contactview(request):
    return render(request,'my_blog/contact.html') 
