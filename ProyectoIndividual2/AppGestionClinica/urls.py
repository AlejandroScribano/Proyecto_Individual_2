from django.urls import path
from AppGestionClinica import views

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('pacientes/', views.pacientes, name="Pacientes"),
    path('doctores/', views.doctores, name="Doctores"),
    path('consultas/', views.consultas, name="Consultas"),
]