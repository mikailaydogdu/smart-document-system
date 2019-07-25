# Generated by Django 2.2.3 on 2019-07-24 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(blank=True, choices=[(1, 'x')], null=True, verbose_name='Dosta Türü')),
                ('label', models.CharField(max_length=36, verbose_name='Döküman Başlık')),
                ('file', models.ImageField(blank=True, null=True, upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim Dosyalarım')),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField(default=256)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Dokuman Ekleme Tarihi')),
                ('revision_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Revizyon Tarihi')),
                ('file_sha1', models.CharField(blank=True, max_length=64, null=True, verbose_name='document_hash')),
                ('follow', models.ManyToManyField(blank=True, related_name='_documents_follow_+', to='documents.Documents')),
            ],
        ),
        migrations.CreateModel(
            name='MyCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32, verbose_name='Dokuman Turu')),
                ('code', models.CharField(max_length=16, verbose_name='Kısa Kodu')),
                ('title', models.CharField(max_length=32, verbose_name='Kod Açıklaması')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Documents')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
