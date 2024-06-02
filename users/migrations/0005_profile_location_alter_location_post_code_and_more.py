# Generated by Django 5.0.3 on 2024-03-24 03:19

import django.db.models.deletion
import localflavor.pk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='post_code',
            field=localflavor.pk.models.PKPostCodeField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=localflavor.pk.models.PKStateField(default='NY', max_length=5),
        ),
    ]