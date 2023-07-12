from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from books.forms import EmpresaForm
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