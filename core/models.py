from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.db import models
# Create your models here.


# ১. ইউনিক ফাইল পাথ তৈরি করার ফাংশনটি মডেলের উপরে রাখতে হবে
def unique_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join('pets/', filename)

    
class pet (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    STATUS_CHOICES = [
         ('available', 'Available'),
        ('pending', 'Pending'),
        ('adopted', 'Adopted'),
    ]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='available')
    image = models.CharField(upload_to = unique_file_path,null=True,blank=True)
