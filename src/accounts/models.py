from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserTable(AbstractUser):
    choices = [(1, 'Erkek'), (2,'Kadın'), (3, 'Belirtmek istemiyor',),]
    ident_no = models.IntegerField(null=True, blank=True, verbose_name='Kimlik No')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    sex = models.IntegerField(null=True, blank=True, choices=choices, verbose_name='Cinsiyet')
    telephone = PhoneNumberField(max_length=13, blank=True, null=True, verbose_name='Telefon No')
    mobile_tel = PhoneNumberField(max_length=13, blank=True, null=True, verbose_name='Telefon No')
    job = models.CharField(max_length=64, null=True, blank=True, verbose_name='Meslek')
    task = models.CharField(max_length=32, null=True, blank=True, verbose_name='Görev')
    image = models.ImageField(null=True, blank=True, verbose_name='Resim')

    def get_ablolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})
