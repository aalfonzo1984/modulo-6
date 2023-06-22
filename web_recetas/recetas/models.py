from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, verbose_name='Nombre de ingrediente')
    imagen = models.ImageField(upload_to='ingredientes', verbose_name='Imagen del ingrediente')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        ordering = ['nombre']
        db_table = 'ingredientes'


class Receta(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de receta')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    preparacion = RichTextField(verbose_name='Modo de Preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name='Imagen')
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['nombre']
        db_table = 'recetas'