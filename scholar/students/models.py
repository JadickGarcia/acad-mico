from django.db import models
class user(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
# Create your models here.
