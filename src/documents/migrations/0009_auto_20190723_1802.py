# Generated by Django 2.2.3 on 2019-07-23 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_auto_20190723_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='hash',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='document_hash'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='type_id',
            field=models.ForeignKey(blank=True, choices=[(1, 'Kalite El Kitabı'), (2, 'Prosedürler'), (3, 'Form'), (4, 'Liste'), (5, 'Görev Tanımı'), (6, 'Proses Haritasi'), (7, 'Şema'), (8, 'Süreç'), (9, 'Talimat'), (10, 'Plan')], null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.my_codes', verbose_name='Dosta Türü'),
        ),
        migrations.DeleteModel(
            name='Documents_Hash',
        ),
    ]
