# Generated by Django 4.0.10 on 2024-11-26 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twit', '0003_rename_text_comment_body_rename_article_comment_twit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
