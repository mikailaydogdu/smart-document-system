from django.db import models

# from accounts.models import CustomUser
from django.conf import settings
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


"""
type_id de choices a dinamik liste göndermek için
yapılan küçük bir döngü
"""



class Documents(models.Model):
    """
    Document Master table dökümana ait
    genel bilgilerin bulunduğu table

    """
    choices = Kodlar(MyCodes, 'DOC')
    # choices = [(1, 'x')]
    label = models.CharField(max_length=36, verbose_name='Döküman Başlık')
    type = models.IntegerField(null=True, blank=True, verbose_name='Dosta Türü', choices=choices)
    comment = models.TextField(default=256)
    active = models.BooleanField(default=True)
    follow = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.label

#
class DocumentDetails(models.Model):
    """
    Kullanıcıların eklemiş oldğu ve
    kullanıcılara göre dökümanlara
    ulaşmak için kullanıdığım table
    """
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE,
                             related_name='user_document')
    file = models.ImageField(upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım', null=True, blank=True)
    file_sha1 = models.CharField(max_length=64, null=True, blank=True, verbose_name='document_hash')
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Dokuman Ekleme Tarihi')
    revision_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Revizyon Tarihi')
    last_open = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.label
