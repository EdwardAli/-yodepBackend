# Generated by Django 4.1.3 on 2022-11-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/testimony'),
        ),
    ]
