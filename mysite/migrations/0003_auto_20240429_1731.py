# Generated by Django 3.1.4 on 2024-04-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
