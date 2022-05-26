import email
from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(primary_key=True, max_length=15, null=False)
    name = models.CharField(max_length=55, null=False)
    surname = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=100,  null=False)
    password=models.CharField(max_length=16, null=False)
