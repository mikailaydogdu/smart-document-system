from django.db import models

# Create your models here.
class mykods(models.Model):
    pass

class user(models.Model):
    pass


class Documents(models.Model):
    """
    Document Master table
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Kullanıcı')
    doc_name = models.CharField(max_length=36, verbose_name='Documnet Name')
    doc_type = models.CharField(max_length=36)


    pass

# class Document_Type(models.Model):
#     pass

class Document_Hash(models.Model):
    doc_id = models.ForeignKey('Documents',on_delete=models.CASCADE, verbose_name='document_id')
    doc_hash = models.CharField(max_length=64, verbose_name='document_hash')

class Document_user(models.Model):
    pass