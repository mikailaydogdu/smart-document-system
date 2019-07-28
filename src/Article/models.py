from django.conf import settings
from django.db import models

from SDS.myFuncitons import Kodlar
from documents.models import MyCodes


class Article(models.Model):
    # choices = Kodlar(MyCodes, 'DOKUMANTYPE')
    # if not choices:
    choices = [(1, 'veri yok')]
    # else:
    #     choices = Kodlar(MyCodes, 'DOKUMANTYPE')
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
    file = models.FileField(upload_to='documents/%Y/%m/%d',
                            verbose_name='Dokuman Path')
    file_sha1 = models.CharField(max_length=32, verbose_name='Benzersiz Kimlik Bilgisi')
    comment = models.TextField(default='dırı vırı ', verbose_name='Dosya Açıklama')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')

    def __str__(self):
        return self.article.title


class Author(models.Model):
    article = models.ManyToManyField(Article, verbose_name='döküman id', related_name="authors")
    auth_name = models.CharField(max_length=32, verbose_name='Tanımı')

    def __str__(self):
        return self.auth_name
