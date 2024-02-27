from django.db import models
from typing import Set
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name