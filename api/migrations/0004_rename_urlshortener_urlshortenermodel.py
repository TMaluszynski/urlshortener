# Generated by Django 4.2.1 on 2023-05-21 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_urlshortener_longurl_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UrlShortener',
            new_name='UrlShortenerModel',
        ),
    ]
