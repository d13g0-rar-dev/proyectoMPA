from django import forms
from .models import Empresa, Empleado



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
 
 
 
class EmpleadoForm(forms.ModelForm):
  class Meta:   
    model = Empleado
    
    fields = {
      "first_name",
      "last_name",
      "tipo_documento",
      "documento",
      "lugar_residencia",
      "fecha_nacimiento", 
      "email", 
      "telefono", 
      "usuario", 
      "password", 
      "empresa", 
    }
    labels = {
      "Nombre Empleado": "first_name",
      "Apellido": "last_name",
      "Tipo de Documento": "tipo_documento",
      "Documento": "documento",
      "Ciudad de Residencia": "lugar_residencia",
      "Fecha de Nacimiento": "fecha_nacimiento",
      "Email": "email",
      "Telefono": "telefono",
      "Usuario": "usuario",
      "Contraseña": "password",
      "Empresa":"empresa",
    }
    widgets = {
      "nombre_empresa" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "nit" : forms.TextInput(attrs={"class": "form-control", "required":""})
    }