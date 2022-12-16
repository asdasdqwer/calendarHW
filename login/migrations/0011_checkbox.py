# Generated by Django 4.0.5 on 2022-10-06 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0010_student_darkmodeenabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkbox_task', to='login.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkbox_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]