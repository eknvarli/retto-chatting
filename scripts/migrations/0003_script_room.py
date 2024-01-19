# Generated by Django 5.0.1 on 2024-01-19 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0009_room_category'),
        ('scripts', '0002_alter_script_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
    ]