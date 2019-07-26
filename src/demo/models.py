from django.conf import settings
from django.db import models


# Create your models here.


class File(models.Model):
    title = models.CharField(max_length=16, verbose_name='Dosya Adı', blank=True, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım', blank=True, null=True)

    def __str__(self):
        return self.file.name





class UserDefinedCode(models.Model):
    name = models.CharField(max_length=8)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Code(models.Model):
    user_defined_code = models.ForeignKey(UserDefinedCode, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=15)

class Document(models.Model):
    title = models.CharField(blank=True, null=True, max_length=200)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)



# https://www.techiediaries.com/django-rest-image-file-upload-tutorial/


