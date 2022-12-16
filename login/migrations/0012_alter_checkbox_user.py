# Generated by Django 4.0.5 on 2022-10-06 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0011_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkbox_user', to=settings.AUTH_USER_MODEL),
        ),
    ]