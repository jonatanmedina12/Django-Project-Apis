from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
timezone.now()

#TODO: modelo de inmueble

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    def __str__(self):
        return  self.nombre


class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,related_name="Empresa_list")
    created = models.DateTimeField(default=timezone.now)  # Usa default en lugar de auto_now_add

    def __str__(self):
        return self.direccion

class Comentario(models.Model):
    calificacion =models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    texto=models.CharField(max_length=200,null=True)
    Inmueble = models.ForeignKey(Inmueble,on_delete=models.CASCADE,related_name='comentarios')
    active =models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)  # Usa default en lugar de auto_now_add
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.calificacion)+" "+ self.Inmueble.direccion