# Generated by Django 4.2.14 on 2024-08-13 10:04

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=users.models.file_upload),
        ),
    ]
