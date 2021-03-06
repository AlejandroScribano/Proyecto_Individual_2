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

def busquedaDoctores(request):
    return render(request, "AppGestionClinica/busquedaDoctores.html")

def buscarDoctores(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        doctores = Doctores.objects.filter(nombre__icontains = nombre)

        return render(request, "AppGestionClinica/resultadoBusqueda.html", {"nombre": nombre, "doctores":doctores})

    else:
        return HttpResponse("Por favor ingrese los datos!")

def leerDoctores(request):
    doctores = Doctores.objects.all()
    contexto = {"doctores": doctores}
    return render(request, "AppGestionClinica/leerDoctores.html", contexto)

def eliminarDoctor(request, doctor_nombre):
    doctor = Doctores.objects.get(nombre=doctor_nombre)
    doctor.delete()

    doctores = Doctores.objects.all()
    contexto = {"doctores": doctores}
    return render(request, "AppGestionClinica/leerDoctores.html", contexto)

def editarDoctor(request, doctor_nombre):
    doctor = Doctores.objects.get(nombre = doctor_nombre)

    if request.method == "POST":
        miFormulario = DoctoresFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            doctor.nombre = informacion['nombre']
            doctor.apellido = informacion['apellido']
            doctor.dia_hora_atencion = informacion['dia_hora_atencion']
            doctor.email = informacion['email']
            doctor.telefono = informacion['telefono']
            doctor.save()

            doctores = Doctores.objects.all()
            contexto = {"doctores": doctores}
            return render(request, "AppGestionClinica/leerDoctores.html",contexto)
        else:
            return HttpResponse("Formulario incorrecto!")

    else:
        miFormulario = DoctoresFormulario(initial = {'nombre': doctor.nombre, 'apellido' : doctor.apellido,
                                                    'dia_hora_atencion' : doctor.dia_hora_atencion, 'email': doctor.email,
                                                    'telefono' : doctor.telefono})

        return render(request, "AppGestionClinica/editarDoctor.html", {"miFormulario": miFormulario, "doctor_nombre" : doctor_nombre})


