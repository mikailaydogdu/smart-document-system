# Generated by Django 2.2.3 on 2019-07-24 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20190724_2101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='file',
            new_name='zfile',
        ),
    ]