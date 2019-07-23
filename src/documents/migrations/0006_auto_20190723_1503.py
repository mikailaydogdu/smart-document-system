# Generated by Django 2.2.3 on 2019-07-23 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0005_auto_20190723_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favori',
            name='doc_id',
        ),
        migrations.AddField(
            model_name='favori',
            name='doc_id',
            field=models.ManyToManyField(blank=True, null=True, to='documents.Documents'),
        ),
        migrations.RemoveField(
            model_name='favori',
            name='user_id',
        ),
        migrations.AddField(
            model_name='favori',
            name='user_id',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]