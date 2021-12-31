from django import forms
from datetime import date, time

from django.forms.forms import Form


class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField(initial=date.today)
    email = forms.EmailField()
    telefono = forms.IntegerField()

class DoctoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dia_hora_atencion = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()

class ConsultasFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha_consulta = forms.DateField(initial=date.today)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    consulta = forms.CharField(max_length=200)