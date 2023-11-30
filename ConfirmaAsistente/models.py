from django.db import models
from django.db.models import Count


# Create your models here.

STATUS_READ = [
    ("d", "Nuevo"),
    ("p", "-"),
]


# Dimension ninio
class d_ninio(models.Model):

    id_ninio = models.AutoField(verbose_name="id_ninio", primary_key=True, db_index=True)
    flag_ninio = models.CharField(verbose_name="flag_ninio", max_length=2)

    def __str__(self):
        return self.flag_ninio


# Dimension vegetariano
class d_vegetariano(models.Model):

    id_vegetarian = models.AutoField(verbose_name="id_veg", primary_key=True, db_index=True)
    flag_vegetarian = models.CharField(verbose_name="flag_vegetariano", max_length=2)

    def __str__(self):
        return self.flag_vegetarian


# Dimension familia
class d_familia(models.Model):
    id_familia = models.AutoField(verbose_name="id_familia", primary_key=True, db_index=True)
    flag_familia = models.CharField(verbose_name="Familia", max_length=50, default="Por Asignar")

    def __str__(self):
        template = 'Mesa {0.flag_familia}'
        return template.format(self)

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"


class d_intolerancias(models.Model):
    id_intolerancias = models.AutoField(verbose_name="id_intolerancias", primary_key=True, db_index=True)
    desc_intolerancias = models.CharField(verbose_name="Tipo", default="Nada", max_length=20)

    def __str__(self):
        return self.desc_intolerancias

    class Meta:
        verbose_name = "Intolerancia"
        verbose_name_plural = "Intolerancias"


class d_contacto(models.Model):

    id_contacto = models.AutoField(verbose_name="id_acompaniante", primary_key=True, db_index=True)
    nombre_contacto = models.CharField(verbose_name="Nombre", max_length=250)
    desc_email = models.EmailField(verbose_name="Email", max_length=50, null=True, unique=True, blank=True)
    desc_telefono = models.CharField(verbose_name="Telefono", max_length=9, null=True, unique=True, blank=True)
    id_intolerancias = models.ForeignKey(d_intolerancias, verbose_name="Intolerancias", on_delete=models.CASCADE, default=1)

    def __str__(self):

        template = '{0.nombre_contacto}'
        return template.format(self)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"


# Fact table
class fact_invitados(models.Model):

    id_invitado = models.AutoField(verbose_name="id_invitado", primary_key=True, db_index=True)
    desc_nombre = models.CharField(verbose_name="Nombre", max_length=250)
    id_contacto = models.ForeignKey(d_contacto, verbose_name="Contacto", on_delete=models.CASCADE)
    id_ninio = models.ForeignKey(d_ninio, verbose_name="Niño", on_delete=models.CASCADE)
    id_vegetarian = models.ForeignKey(d_vegetariano, verbose_name="Vegetariano", on_delete=models.CASCADE)
    id_intolerancias = models.ForeignKey(d_intolerancias, verbose_name="Intolerancias", on_delete=models.CASCADE)
    id_familia = models.ForeignKey(d_familia, verbose_name="Grupo", on_delete=models.CASCADE)
    estado = models.CharField(verbose_name="Estado", choices=STATUS_READ, default="d", max_length=1)

    def __str__(self):
        template = '{0.desc_nombre}'
        return template.format(self)

    class Meta:
        verbose_name = "Invitado"
        verbose_name_plural = "Invitados"
