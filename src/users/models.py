from django.db import models

from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class UserTable(AbstractBaseUser):
    birth_date  = models.DateField()
    telephone   = models.CharField(max_length=11)
    lldatetime    = models.DateTimeField(null=True)
    image       = models.ImageField()
    location    = models.CharField(max_length=32,null=True)
    biographi   = models.TextField(max_length=280, null=True)
