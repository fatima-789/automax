# Generated by Django 5.0.3 on 2024-03-24 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]
