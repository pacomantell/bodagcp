# Generated by Django 4.2.1 on 2023-07-26 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0015_alter_playlist_artista_alter_playlist_nombre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayList',
        ),
    ]