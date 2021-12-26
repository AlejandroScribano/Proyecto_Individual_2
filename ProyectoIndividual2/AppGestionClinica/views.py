from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"AppGestionClinica/inicio.html")

def pacientes(request):
    return render(request, "AppGestionClinica/pacientes.html")

def doctores(request):
    return render(request, "AppGestionClinica/doctores.html")

def consultas(request):
    return render(request, "AppGestionClinica/consultas.html")