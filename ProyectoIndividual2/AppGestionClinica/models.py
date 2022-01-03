from django.db import models
from django.db.models.base import Model

# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de nacimiento: {self.fecha_nacimiento} - email: {self.email}"

class Doctores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dia_hora_atencion = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Día y hora de atención: {self.dia_hora_atencion} - email: {self.email} - Telefono: {self.telefono}"

class Consultas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_consulta = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()
    consulta = models.CharField(max_length=200)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - email: {self.email} - Fecha de consulta: {self.fecha_consulta} - Consulta: {self.consulta}"


