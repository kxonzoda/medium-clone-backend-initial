# Generated by Django 4.2.14 on 2024-08-13 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='user',
        ),
    ]
