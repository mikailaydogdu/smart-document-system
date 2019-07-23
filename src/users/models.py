from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserTable(AbstractUser):
    birth_date  = models.DateField(blank=True, verbose_name='Doğum Tarihi')
    telephone   = models.CharField(max_length=11, blank=True, verbose_name='Telefon No')
    image       = models.ImageField(blank=True, verbose_name='Resim')

    # def generate_password(self):
    #     self.password