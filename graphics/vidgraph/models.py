from django.db import models
from typing import Set
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title=models.CharField(max_length=500)
    # image=models.ImageField(upload_to='image',blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
class Comment(models.Model):
    post=models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=100)
    body=models.TextField()
    added_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s -%s' % (self.post.title,self.name)
    
    def TotalComment(self):
        return self.comments.count()

    def comments(self):
        return reverse("blog-single",kwargs={"slug":self.id}) 