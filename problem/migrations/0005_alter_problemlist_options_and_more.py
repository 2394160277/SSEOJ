# Generated by Django 5.1.2 on 2024-11-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_alter_problemlist_difficulty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problemlist',
            options={},
        ),
        migrations.RemoveField(
            model_name='problemlist',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='problemlist',
            name='last_update_time',
        ),
        migrations.AddField(
            model_name='problemlist',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problemlist',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
