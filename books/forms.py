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
      "nombre",
      "apellido",
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
      "Nombre": "nombre",
      "Apellido": "apellido",
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
      "nombre" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "apellido" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "tipo_documento" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "documento" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "lugar_residencia" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "fecha_nacimiento" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "email" : forms.EmailInput(attrs={"class": "form-control", "required":""}),
      "telefono" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "usuario" : forms.TextInput(attrs={"class": "form-control", "required":""}),
      "password" : forms.PasswordInput(attrs={"class": "form-control", "required":""}),
      "empresa" : forms.TextInput(attrs={"class": "form-control", "required":""})
    }