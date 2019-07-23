from django.db import models
from src.users.models import UserTable

# Create your models here.
class my_codes(models.Model):
    pass


class Documents(models.Model):
    """
    Document Master table
    """
    doc_name    = models.CharField(max_length=36, verbose_name='Documnet Name')
    doc         = models.FileField()
    doc_type    = models.CharField(max_length=36)
    doc_date    = models.DateTimeField(auto_now_add=True)


    pass

# class Document_Type(models.Model):
#     pass

class Documents_Hash(models.Model):
    doc_id      = models.ForeignKey('Documents',on_delete=models.CASCADE, verbose_name='document_id')
    doc_hash    = models.CharField(max_length=64, verbose_name='document_hash')

class Documents_user(models.Model):
    user_id = models.ForeignKey('UserTable', on_delete=models.CASCADE)
    doc_id = models.ForeignKey('Documents', on_delete=models.CASCADE)