# Generated by Django 5.1.2 on 2024-12-09 14:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.CharField(db_index=True, default=uuid.UUID('e223837d-109a-4a2e-b43e-7fd8a761196c'), max_length=36, primary_key=True, serialize=False),
        ),
    ]