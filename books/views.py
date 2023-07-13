from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from books.forms import EmpresaForm, EmpleadoForm
from .models import Empresa, Empleado


# Create your views here.
def empresas(request):
  empresas = Empresa.objects.all()
  template = loader.get_template("books/empresas.html")
  context = {"empresas":empresas,}
  return HttpResponse(template.render(context,request))

def empleados(request):
  empleados= Empleado.objects.all() 
  template = loader.get_template("books/empleados.html")
  context = {"empleados":empleados,}
  return HttpResponse(template.render(context,request))  

def home(request):
  template=loader.get_template("index.html")
  context={}
  return HttpResponse(template.render(context,request))


def new_Empresa(request):
  if request.method == "POST":
    form = EmpresaForm(request.POST)
    if form.is_valid():
      nombre = form.cleaned_data["nombre_empresa"]
      nit = form.cleaned_data["nit"]
      empresa = Empresa(nombre_empresa = nombre , nit = nit)
      empresa.save()
      return HttpResponseRedirect(reverse("empresas"))
  else:
    form = EmpresaForm()
  return render(request, "books/create_empresas.html", {"form":form})


def new_Empleado(request):
  if request.method == "POST":
    form = EmpleadoForm(request.POST)
    if form.is_valid():
      nombre = form.cleaned_data["nombre"]
      apellido = form.cleaned_data["apellido"]
      tipo_documento = form.cleaned_data["tipo_documento"]
      documento = form.cleaned_data["documento"]
      lugar_residencia = form.cleaned_data["lugar_residencia"]
      fecha_nacimiento = form.cleaned_data["fecha_nacimiento"]
      email = form.cleaned_data["email"]
      telefono = form.cleaned_data["telefono"]
      usuario = form.cleaned_data["usuario"]
      password = form.cleaned_data["password"]
      empresa = form.cleaned_data["empresa"]
      empleado = Empleado(nombre = nombre , apellido = apellido, tipo_documento=tipo_documento, documento=documento,lugar_residencia=lugar_residencia, fecha_nacimiento=fecha_nacimiento,email=email,telefono=telefono,usuario=usuario,password=password, empresa=empresa)
      empleado.save()
      return HttpResponseRedirect(reverse("empleados"))
  else:
    form = EmpleadoForm()
  return render(request, "books/create_empleados.html", {"form":form})

def integrantes(request):
  template=loader.get_template("books/integrantes.html")
  context={}
  return HttpResponse(template.render(context,request))