# Generated by Django 5.0.3 on 2024-03-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=150)),
                ('address_2', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]