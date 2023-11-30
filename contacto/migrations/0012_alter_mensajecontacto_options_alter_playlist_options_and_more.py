# Generated by Django 4.2.1 on 2023-07-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0011_mensajecontacto_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensajecontacto',
            options={'verbose_name': 'Mensaje', 'verbose_name_plural': 'Mensajes'},
        ),
        migrations.AlterModelOptions(
            name='playlist',
            options={'verbose_name': 'Canción', 'verbose_name_plural': 'Canciones'},
        ),
        migrations.AddField(
            model_name='playlist',
            name='estado',
            field=models.CharField(choices=[('d', 'No leído'), ('p', 'Leído')], default='d', max_length=1, verbose_name='Estado'),
        ),
    ]
