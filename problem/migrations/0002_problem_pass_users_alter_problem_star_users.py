# Generated by Django 5.1.2 on 2024-11-11 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='pass_users',
            field=models.ManyToManyField(related_name='pass_problems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='problem',
            name='star_users',
            field=models.ManyToManyField(related_name='star_problems', to=settings.AUTH_USER_MODEL),
        ),
    ]