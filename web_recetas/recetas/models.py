from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, verbose_name='Nombre de ingrediente')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        ordering = ['nombre']
        db_table = 'ingredientes'


class Receta(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de receta')
    descripcion = models.CharField(max_length=250, verbose_name='Descripción')
    preparacion = models.TextField(verbose_name='Modo de Preparación')
    imagen = models.ImageField(upload_to='recetas')
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['nombre']
        db_table = 'recetas'