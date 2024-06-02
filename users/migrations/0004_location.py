# Generated by Django 5.0.3 on 2024-03-24 03:08

import localflavor.pk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=150)),
                ('address_2', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', localflavor.pk.models.PKStateField(max_length=5)),
                ('post_code', localflavor.pk.models.PKPostCodeField(max_length=5)),
            ],
        ),
    ]