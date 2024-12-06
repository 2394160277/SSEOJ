# Generated by Django 4.2.16 on 2024-11-18 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcomment",
            name="reply_to_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reply_to_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
