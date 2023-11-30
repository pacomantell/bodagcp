# Generated by Django 4.2.1 on 2023-06-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id_cancion', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_cancion')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre_cancion')),
                ('artista', models.CharField(max_length=250, verbose_name='nombre_artista')),
            ],
        ),
    ]
