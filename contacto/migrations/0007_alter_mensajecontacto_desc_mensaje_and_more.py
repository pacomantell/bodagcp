# Generated by Django 4.2.1 on 2023-06-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0006_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajecontacto',
            name='desc_mensaje',
            field=models.TextField(max_length=500, verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='desc_nombre',
            field=models.CharField(max_length=250, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
    ]
