from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    birth_date  = models.DateField(null=True,blank=True, verbose_name='Doğum Tarihi')
    telephone   = models.CharField(null=True,max_length=11, blank=True, verbose_name='Telefon No')
    image       = models.ImageField(null=True,blank=True, verbose_name='Resim')
    follow      = models.ManyToManyField('self',blank=True)