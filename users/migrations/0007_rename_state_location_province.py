# Generated by Django 5.0.3 on 2024-04-01 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='state',
            new_name='province',
        ),
    ]