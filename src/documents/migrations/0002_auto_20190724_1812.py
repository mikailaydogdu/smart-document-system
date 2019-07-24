# Generated by Django 2.2.3 on 2019-07-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='doc',
        ),
        migrations.AddField(
            model_name='documents',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d', verbose_name='Dokumanlarım'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='type_id',
            field=models.IntegerField(blank=True, choices=[(1, 'Kalite El Kitabı'), (2, 'Prosedürler'), (3, 'Form'), (4, 'Liste'), (5, 'Görev Tanımı'), (6, 'Proses Haritasi'), (7, 'Şema'), (8, 'Süreç'), (9, 'Talimat'), (10, 'Plan')], null=True, verbose_name='Dosta Türü'),
        ),
    ]