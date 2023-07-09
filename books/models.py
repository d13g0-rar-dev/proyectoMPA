from django.db import models

# Modelo para la entidad TipoDocumento.
class TipoDocumento(models.Model):
  nombre_tipo = models.CharField(max_length=30)
  descripcion_tipo = models.CharField(max_length=300)
  
# Modelo para la entidad Ciudad.
class Ciudad(models.Model):
  nombre_ciudad = models.CharField(max_length=30)
  descripcion_ciudad = models.CharField(max_length=300)

# Modelo para la entidad Empresa.
class Empresa(models.Model):
  nombre_empresa = models.CharField(max_length=30)
  nit = models.IntegerField()

# Modelo para la entidad Empleado.
class Empleado(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
  documento = models.IntegerField()
  lugar_residencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
  fecha_nacimiento = models.DateField(null=True)
  email = models.EmailField(max_length=50)
  telefono = models.IntegerField()
  usuario = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

