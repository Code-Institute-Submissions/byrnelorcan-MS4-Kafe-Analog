# Generated by Django 3.2.8 on 2021-10-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211019_2132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vinyl',
            new_name='Products',
        ),
        migrations.DeleteModel(
            name='Coffee',
        ),
    ]
