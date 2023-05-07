from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='categoria_imagenes', blank=True, null=True)
    background = models.ImageField(upload_to='categoria_imagenes', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    categoria = models.ForeignKey(Categoria, related_name = 'categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='juego_imagenes', blank=True, null=True)

    class Meta:
        ordering=('nombre', )

    def __str__(self):
        return self.nombre

    
