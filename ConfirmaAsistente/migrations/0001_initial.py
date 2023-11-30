# Generated by Django 4.2.1 on 2023-08-01 08:05

from django.db import migrations, models
import django.db.models.deletion


def populate_dim(apps, schema_editor):
    flags = ['No', 'Sí']
    Ninio = apps.get_model('ConfirmaAsistente', 'd_ninio')
    Vegetariano = apps.get_model('ConfirmaAsistente', 'd_vegetariano')
    for flag in flags:
        obj1 = Ninio(flag_ninio=flag)
        obj2 = Vegetariano(flag_vegetarian=flag)
        obj1.save()
        obj2.save()

    intoler = ['Nada', 'Gluten', 'Lactosa', 'Marisco', 'Sulfitos', 'Otras']
    Intolerancia = apps.get_model('ConfirmaAsistente', 'd_intolerancias')
    for i in intoler:
        obj = Intolerancia(desc_intolerancias=i)
        obj.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='d_contacto',
            fields=[
                ('id_contacto', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_acompaniante')),
                ('nombre_contacto', models.CharField(max_length=250, verbose_name='Nombre')),
                ('desc_email', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Email')),
                ('desc_telefono', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='d_familia',
            fields=[
                ('id_familia', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_familia')),
                ('flag_familia', models.CharField(default='Por Asignar', max_length=50, verbose_name='Familia')),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
            },
        ),
        migrations.CreateModel(
            name='d_intolerancias',
            fields=[
                ('id_intolerancias', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_intolerancias')),
                ('desc_intolerancias', models.CharField(default='Nada', max_length=20, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Intolerancia',
                'verbose_name_plural': 'Intolerancias',
            },
        ),
        migrations.CreateModel(
            name='d_ninio',
            fields=[
                ('id_ninio', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_ninio')),
                ('flag_ninio', models.CharField(max_length=2, verbose_name='flag_ninio')),
            ],
        ),
        migrations.CreateModel(
            name='d_vegetariano',
            fields=[
                ('id_vegetarian', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_veg')),
                ('flag_vegetarian', models.CharField(max_length=2, verbose_name='flag_vegetariano')),
            ],
        ),
        migrations.CreateModel(
            name='fact_invitados',
            fields=[
                ('id_invitado', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id_invitado')),
                ('desc_nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('estado', models.CharField(choices=[('d', 'Nuevo'), ('p', '-')], default='d', max_length=1, verbose_name='Estado')),
                ('id_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfirmaAsistente.d_contacto', verbose_name='Contacto')),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfirmaAsistente.d_familia', verbose_name='Grupo')),
                ('id_intolerancias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfirmaAsistente.d_intolerancias', verbose_name='Intolerancias')),
                ('id_ninio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfirmaAsistente.d_ninio', verbose_name='Niño')),
                ('id_vegetarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfirmaAsistente.d_vegetariano', verbose_name='Vegetariano')),
            ],
            options={
                'verbose_name': 'Invitado',
                'verbose_name_plural': 'Invitados',
            },
        ),
        migrations.RunPython(populate_dim),
    ]
