from django.db import models
from pip._vendor.msgpack.fallback import xrange
from django.db import connection

from users.models import UserTable



# Create your models here.
class my_codes(models.Model):
    """
    Kodların tutulduğu table
    """
    type    = models.CharField(max_length=32, verbose_name='Dokuman Turu')
    code    = models.CharField(max_length=16, verbose_name='Kısa Kodu')
    title   = models.CharField(max_length=32, verbose_name='Kod Açıklaması')

    def __str__(self):
        return self.title

# x  = my_codes.objects.all().filter(type='DOKUMAN')
#
# for i in x:
#     print(i)

#
# with connection.cursor() as cursor:
#     cursor.execute('select cc.id,cc.title from documents_my_codes cc where cc.type="DOKUMAN"')
#     result = cursor.fetchall()
#
# xchoices = ()
# for i in result:
#     xchoices +=i
#
# print(xchoices)

xchoices = ((1, 'Kalite El Kitabı'), (2, 'Prosedürler'),(3, 'Form'), (4, 'Liste'), (5, 'Görev Tanımı'), (6, 'Proses Haritasi'),( 7, 'Şema'),( 8, 'Süreç'),
            (9, 'Talimat'), (10, 'Plan'))

class Documents(models.Model):
    """
    Document Master table dökümana ait
    genel bilgilerin bulunduğu table

    """

    type_id = models.ForeignKey(my_codes , null=True, blank=True, on_delete=models.CASCADE,verbose_name='Dosta Türü', choices=xchoices)
    title           = models.CharField(max_length=36, verbose_name='Döküman Başlık')
    doc             = models.FileField(verbose_name='Dokumanlarım')
    image           = models.ImageField(verbose_name='Resim Dosyalarım',null=True,blank=True)
    active          = models.BooleanField(default=True)
    comment         = models.TextField(default=256)
    create_date     = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Dokuman Ekleme Tarihi')
    revision_date   = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Revizyon Tarihi')
    hash            = models.CharField(max_length=64,null=True,blank=True ,verbose_name='document_hash')
    fallow          = models.ManyToManyField('self')


    def __str__(self):
        return self.title


class Documents_user(models.Model):
    """
    Kullanıcıların eklemiş oldğu ve
    kullanıcılara göre dökümanlara
    ulaşmak için kullanıdığım table
    """
    user_id     = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    doc_id      = models.ForeignKey(Documents, on_delete=models.CASCADE)

