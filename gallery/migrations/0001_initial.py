# Generated by Django 2.2.8 on 2022-05-30 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=30)),
                ('photo_description', models.TextField()),
                ('Photo', models.ImageField(default='image.jpg', upload_to='images/')),
                ('photo_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gallery.Category')),
                ('photo_location', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Location')),
            ],
        ),
    ]