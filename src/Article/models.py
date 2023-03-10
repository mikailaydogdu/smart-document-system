from django.conf import settings
from django.db import models
from django.utils import timezone


from SDS.myFuncitons import Kodlar


class MyCodes(models.Model):
    """
    Kodların tutulduğu table
    """
    type = models.CharField(max_length=32, verbose_name='Dokuman Turu')
    code = models.CharField(max_length=16, verbose_name='Kısa Kodu')
    title = models.CharField(max_length=32, verbose_name='Kod Açıklaması')

    def __str__(self):
        return self.title


class Article(models.Model):
    choices = Kodlar(MyCodes, 'DOKUMANTYPE')
    if not choices:
        choices = [(1, 'veri yok')]
    else:
        choices = Kodlar(MyCodes, 'DOKUMANTYPE')
    title = models.CharField(max_length=32, null=False, blank=False, verbose_name='Dosya Adı')
    type = models.IntegerField(null=True, blank=True, choices=choices, verbose_name='Dosta Türü')
    active = models.BooleanField(default=True, verbose_name='Aktif/Pasif')

    def __str__(self):
        return self.title


class Revisions(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name='Döküman id', related_name='revision_article')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 verbose_name='Döküman Ekleyen', related_name='revision_uploader')
    file = models.FileField(upload_to='document/%Y/%m/%d',
                            verbose_name='Dokuman Path')
    file_sha1 = models.CharField(max_length=32, verbose_name='Benzersiz Kimlik Bilgisi')
    comment = models.TextField(default='dırı vırı ', verbose_name='Dosya Açıklama')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')

    def __str__(self):
        return self.comment


class Author(models.Model):
    article = models.ManyToManyField(Article, verbose_name='döküman id', related_name="authors")
    auth_name = models.CharField(max_length=32, verbose_name='Tanımı')

    def __str__(self):
        return self.auth_name


# from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
