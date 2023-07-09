from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Empleado

# Create your views here.
def index(request):
  empleados = Empleado.objects.all()
  template = loader.get_template("books/index.html")
  context = {
    "empleados":empleados,
  }
  return HttpResponse(template.render(context,request))