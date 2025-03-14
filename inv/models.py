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

    def save(self):
        self.descripcion = self.descripcion.capitalize() #Coloca la descripcion con la primera letra en mayuscula
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la Categoria'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.capitalize()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria', 'descripcion') #Unique Compuesto


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Nombre de la Marca',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.capitalize()
        super(Marca, self).save()

    class Meta():
        verbose_name_plural = 'Marcas'



class UM(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Nombre de la Unidad de Medida',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.capitalize()
        super(UM, self).save()

    class Meta():
        verbose_name_plural = 'Unidades de Medida'



class Producto(ClaseModelo):
    codigo = models.CharField(max_length = 100, unique = True)
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    unidad_medida = models.ForeignKey(UM, on_delete = models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.capitalize()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo', 'codigo_barra')