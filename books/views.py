from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Empresa

# Create your views here.
def empresas(request):
  empresas = Empresa.objects.all()
  template = loader.get_template("books/empresas.html")
  context = {"empresas":empresas,}
  return HttpResponse(template.render(context,request))


def home(request):
  template=loader.get_template("index.html")
  context={}
  return HttpResponse(template.render(context,request))