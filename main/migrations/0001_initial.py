# Generated by Django 5.0.3 on 2024-04-01 01:48

import django.db.models.deletion
import main.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cateogory', models.CharField(choices=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction'), ('childrens-books', "Children's Books"), ('educational-reference', 'Educational/Reference'), ('poetry', 'Poetry'), ('drama-play', 'Drama/Play'), ('comics-graphic-novels', 'Comics/Graphic Novels'), ('magazines-journals', 'Magazines/Journals'), ('religious-spiritual-texts', 'Religious/Spiritual Texts'), ('fantasy-science-fiction', 'Fantasy/Science Fiction'), ('romance', 'Romance'), ('mystery-thriller', 'Mystery/Thriller'), ('biography-autobiography', 'Biography/Autobiography'), ('health-wellness', 'Health/Wellness'), ('environmental-science', 'Environmental/Science')], default=None, max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('condition', models.CharField(choices=[('old', 'Old'), ('new', 'New')], default=None, max_length=24)),
                ('image', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
