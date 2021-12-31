from django.shortcuts import render
from django.http import HttpResponse
from AppGestionClinica.forms import PacientesFormulario, DoctoresFormulario, ConsultasFormulario
from AppGestionClinica.models import Pacientes, Doctores, Consultas

# Create your views here.

def inicio(request):
    return render(request,"AppGestionClinica/inicio.html")

def pacientes(request):

    if request.method == "POST":

        miFormulario = PacientesFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            instaPaciente = Pacientes(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                fecha_nacimiento = informacion["fecha_nacimiento"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            instaPaciente.save()
            return render(request, "AppGestionClinica/inicio.html")
    else:
        miFormulario = PacientesFormulario()
        return render(request, "AppGestionClinica/pacientes.html", {"miFormulario":miFormulario})


def doctores(request):
    if request.method == "POST":

        miFormulario = DoctoresFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            instaPaciente = Doctores(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                dia_hora_atencion = informacion["dia_hora_atencion"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            instaPaciente.save()
            return render(request, "AppGestionClinica/inicio.html")
    else:
        miFormulario = DoctoresFormulario()
        return render(request, "AppGestionClinica/doctores.html", {"miFormulario":miFormulario})


def consultas(request):
    if request.method == "POST":

        miFormulario = ConsultasFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            instaPaciente = Consultas(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                fecha_consulta = informacion["fecha_consulta"],
                email = informacion["email"],
                telefono = informacion["telefono"],
                consulta = informacion["consulta"]
            )
            instaPaciente.save()
            return render(request, "AppGestionClinica/inicio.html")
    else:
        miFormulario = ConsultasFormulario()
        return render(request, "AppGestionClinica/consultas.html", {"miFormulario":miFormulario})