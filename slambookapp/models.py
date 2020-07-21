from django.db import models
from datetime import datetime

# Create your models here.
class Fillup(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Nickname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos/')
    phone=models.IntegerField()
    add=models.TextField()
    dob=models.CharField(max_length=200)
    zodiac=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    fathername=models.CharField(max_length=200)
    mothername=models.CharField(max_length=200)
    brothername=models.CharField(max_length=200)
    sistername=models.CharField(max_length=200)
    Bestfriendname=models.CharField(max_length=200)
    twitter=models.CharField(max_length=200)
    facebook=models.CharField(max_length=200)
    instagram=models.CharField(max_length=200)
    txtmail=models.CharField(max_length=200)
    about=models.TextField()
    Relation=models.CharField(max_length=200)
    likes=models.CharField(max_length=200)
    suggestions=models.TextField()
    postdate= models.DateTimeField(default=datetime.now, blank=True)
