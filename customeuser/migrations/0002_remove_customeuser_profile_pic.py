# Generated by Django 4.2.4 on 2023-08-22 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customeuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeuser',
            name='profile_pic',
        ),
    ]
