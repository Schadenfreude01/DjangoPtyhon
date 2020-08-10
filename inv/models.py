from django.db import models

from bases.models import ClaseModelo
# Create your models here.

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la Categoria',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    # def save(self):
    #     self.descripcion = self.descripcion.upper() #Guardar la descripcion el mayuscula
    #     super(Categoria.descripcion).save()

    class Meta:
        verbose_name_plural = 'Categorias'