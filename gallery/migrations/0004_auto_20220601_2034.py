# Generated by Django 2.2.8 on 2022-06-01 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20220531_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='photo_category',
            new_name='photocategory',
        ),
    ]
