from django.db import models
from django.db.models.base import Model

# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()

class Doctores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dia_hora_atencion = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_consulta = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()
    consulta = models.CharField(max_length=200)


