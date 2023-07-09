from django.db import models

# Modelo para la entidad TipoDocumento.
class TipoDocumento(models.Model):
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=300)
  
# Modelo para la entidad Ciudad.
class Ciudad:
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=300)

# Modelo para la entidad Empresa.
class Empresa(models.Model):
  nombre = models.CharField(max_length=30)
  nit = models.IntegerField(max_length=10)

# Modelo para la entidad Empleado.
class Empleado(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
  documento = models.IntegerField(max_length=10)
  lugar_residencia = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
  fecha_nacimiento = models.DateField(null=True)
  email = models.EmailField(max_length=50)
  telefono = models.IntegerField(max_length=10)
  usuario = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

