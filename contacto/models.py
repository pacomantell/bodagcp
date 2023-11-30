from django.db import models

# Create your models here.

STATUS_READ = [
    ("d", "No leído"),
    ("p", "Leído"),
]


class MensajeContacto(models.Model):

    desc_nombre = desc_nombre = models.CharField(verbose_name="Nombre", max_length=250)
    email = models.EmailField(verbose_name="Email", max_length=50, null=False)
    desc_mensaje = models.TextField(verbose_name="Mensaje", max_length=500,)
    estado = models.CharField(verbose_name="Estado", choices=STATUS_READ, default="d", max_length=1)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):

        template = 'Mensaje de {0.desc_nombre}'
        return template.format(self)
