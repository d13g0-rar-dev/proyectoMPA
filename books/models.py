from django.db import models

# Modelo para la entidad TipoDocumento.
class TipoDocumento(models.Model):
  nombre_tipo = models.CharField(max_length=300, primary_key=True)
  
# Modelo para la entidad Ciudad.
class Ciudad(models.Model):
  nombre_ciudad = models.CharField(max_length=300, primary_key=True)

# Modelo para la entidad Empresa.
class Empresa(models.Model):
  nombre_empresa = models.CharField(max_length=300, primary_key=True)
  nit = models.IntegerField()

# Modelo para la entidad Empleado.
class Empleado(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  tipo_documento = models.ForeignKey(TipoDocumento,  on_delete=models.CASCADE)
  documento = models.BigIntegerField()
  lugar_residencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
  fecha_nacimiento = models.DateField()
  email = models.EmailField(max_length=50)
  telefono = models.BigIntegerField()
  usuario = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

