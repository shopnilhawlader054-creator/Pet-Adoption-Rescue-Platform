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

    
class Pet (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    STATUS_CHOICES = [
         ('available', 'Available'),
        ('pending', 'Pending'),
        ('adopted', 'Adopted'),
    ]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='available')
    image = models.ImageField(max_length=500,upload_to = unique_file_path,null=True,blank=True)
    age = models.CharField(max_length=50,null=False,blank=False)
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
    ]
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES,null=False,blank=False)
    ANIMAL_TYPES = [
    ('dog', 'Dog'),
    ('cat', 'Cat'),
    ('bird', 'Bird'),
    ('others','Others'),
]
    animal_type = models.CharField(max_length=50,choices=ANIMAL_TYPES)
    breed = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    descraption = models.CharField(max_length=200,null=True,blank=False)
    creat_at = models.DateTimeField(auto_now_add= True)

class Adoptions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='adoptions_user')
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE,related_name='adoptions_user')
    phone = models.CharField(max_length=15)
    STATUS_CHOICES = [
             ('available', 'Available'),
            ('pending', 'Pending'),
            ('adopted', 'Adopted'),
        ]
    adders = models.CharField(max_length=200)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    reson = models.TextField()
    previous_pet_experience = models.BooleanField(default=False)
    created_add = models.DateTimeField(auto_now_add=True)
