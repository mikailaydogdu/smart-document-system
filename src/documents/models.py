from django.db import models
from users.models import UserTable


# Create your models here.
class my_codes(models.Model):
    """
    Kodların tutulduğu tablom burada
    """
    type    = models.CharField(max_length=32, verbose_name='Dokuman Turu')
    code    = models.CharField(max_length=16, verbose_name='Kısa Kodu')
    title   = models.CharField(max_length=32, verbose_name='Kod Açıklaması')


class Documents(models.Model):
    """
    Document Master table dökümana ait genel bilgilerin bulunduğu table
    """
    title       = models.CharField(max_length=36, verbose_name='Döküman Başlık')
    doc         = models.FileField(verbose_name='Dosya')
    type        = models.CharField(max_length=36, verbose_name='Dosta Türü')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Dokuman Ekleme Tarihi')
    active      = models.BooleanField(default=True)

class Documents_Hash(models.Model):
    """
    Document hash table yeni bir döküman ekleme sırasın eklenen dökümanla var olan döküman ın
    hash bilgisine bakmak için gerekli gördüğüm table
    """
    doc_id      = models.ForeignKey(Documents,on_delete=models.CASCADE, verbose_name='document_id')
    doc_hash    = models.CharField(max_length=64, verbose_name='document_hash')

class Documents_user(models.Model):
    """
    Kullanıcıların eklemiş oldğu ve kullanıcılara göre dökümanlara ulaşmak için kullanıdığım table
    """
    user_id     = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    doc_id      = models.ForeignKey(Documents, on_delete=models.CASCADE)