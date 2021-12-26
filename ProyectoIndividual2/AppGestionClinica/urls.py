from django.urls import path
from AppGestionClinica import views

urlpatterns = [
    path('',views.inicio),
]