# Generated by Django 4.0.10 on 2024-11-26 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twit', '0004_twit_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_twits', to=settings.AUTH_USER_MODEL),
        ),
    ]