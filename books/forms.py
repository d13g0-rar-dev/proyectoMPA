from django import forms
from .models import Empresa



class EmpresaForm(forms.ModelForm):
  class Meta:
    
    model = Empresa
    
    fields = {
      "nombre_empresa",
      "nit",
    }
    labels = {
      "Nombre Empresa": "nombre_empresa",
      "NIT": "nit",
    }
    widgets = {
      "nombre_empresa" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "nit" : forms.TextInput(attrs={"class": "form-control", "required":""})
    }
    
