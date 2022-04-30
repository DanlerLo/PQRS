from email.policy import default
from sqlite3 import Timestamp
from time import timezone
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.
class Vinculo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
opciones_vinculo = [
    [0,"directivos"],
    [1,"docentes"],
    [2,"administrativos"],
    [3,"padre de familia"],
    [4,"estudiante"],
    [5,"otros"]
]
opciones_peticion = [
    [2,"peticion"],
    [3,"queja"],
    [4,"sugerencia"],
    [5,"reconocimiento"]
]
class registro(models.Model):
    Fecha = models.DateField(auto_now=False)
    Radicado = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Grado_o_area = models.CharField(max_length=50)
    Email = models.EmailField()
    vinculo = models.IntegerField(choices=opciones_vinculo)
    tipo = models.IntegerField(choices=opciones_peticion)
    Dependencia = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=50)
    Deescripcion = models.TextField()
    Terminos_y_condiciones = models.ForeignKey(Vinculo, on_delete=models.PROTECT)

    def __str__(self):
        return self.Nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='cosfa.png')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

class Post(models.Model):
	usuario = models.ForeignKey(
	    User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.usuario.username}: {self.content}'

    
