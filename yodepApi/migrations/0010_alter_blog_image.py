# Generated by Django 4.1.3 on 2022-11-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0009_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/blog'),
        ),
    ]
