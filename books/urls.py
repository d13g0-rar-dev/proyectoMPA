from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  #path("templates/books/", views.index, name="index"),
  path("empresas/", views.empresas, name="empresas"),
  path("empresas/new/", views.new_Empresa, name="new_Empresa"),
  path("empleados/", views.empleados, name="empleados"),
  path("empleados/new/", views.new_Empleado, name="new_Empleado"),
  path("tiposDocumento/", views.tipoDocumento, name="tiposDocumento"),
  path("ciudades/", views.ciudad, name="ciudades"),
  path("integrantes/", views.integrantes, name="integrantes"),
]