# Generated by Django 4.1.3 on 2022-11-24 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yodepApi', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phyAddress', models.CharField(max_length=250)),
                ('attachedFile', models.FileField(max_length=254, upload_to='files/career')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
