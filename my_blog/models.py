from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    token = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts',null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
