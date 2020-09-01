from django.db import models

from bases.models import ClaseModelo
# Create your models here.

class Proveedor(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        unique=True
    )
    direccion = models.CharField(
        max_length=250,
        blank=True, null=True
    )
    contacto = models.CharField(
        max_length=100
    )
    telefono = models.CharField(
        max_length=10,
        blank=True, null=True
    )
    email = models.CharField(
        max_length=250,
        blank=True, null=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.capitalize()
        super(Proveedor, self).save()

    class Meta():
        verbose_name_plural = 'Proveedores'