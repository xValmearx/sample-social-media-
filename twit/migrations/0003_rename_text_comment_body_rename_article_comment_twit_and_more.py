# Generated by Django 4.0.10 on 2024-11-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='twit',
        ),
        migrations.RenameField(
            model_name='twit',
            old_name='Author',
            new_name='author',
        ),
    ]