# Generated by Django 4.1.1 on 2022-09-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='roomName',
        ),
    ]