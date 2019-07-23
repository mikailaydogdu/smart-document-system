# Generated by Django 2.2.3 on 2019-07-23 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20190723_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favori',
            name='doc_id',
            field=models.ManyToManyField(blank=True, to='documents.Documents'),
        ),
        migrations.AlterField(
            model_name='favori',
            name='user_id',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]