# Generated by Django 4.2.5 on 2023-09-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='default_product_photo.jpg', upload_to='product_photos/'),
        ),
    ]
