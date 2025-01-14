from django.db import models
from typing import Set
from django.db import models
from django.shortcuts import reverse
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Comment(models.Model):
    post=models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    first_name=models.CharField(max_length=100)
    body=models.TextField()
    added_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s -%s' % (self.post.title,self.first_name)
    
    def TotalComment(self):
        return self.comments.count()

    def comments(self):
        return reverse("blog-detail",kwargs={"id":self.pk}) 
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None  # Remove the username field
    # first_name=None
    # last_name=None
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=200)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name
class Blog(models.Model):
    title=models.CharField(max_length=500)
    # image=models.ImageField(upload_to='image',blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    def __str__(self):
        return self.title
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class Video(models.Model):
    myvideo=models.FileField(upload_to='video/')
    title=models.CharField(max_length=300)
    created_on=models.DateTimeField(auto_now_add=True)
    Author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title