# Generated by Django 2.2.8 on 2022-05-30 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='Photo',
            new_name='photo',
        ),
    ]