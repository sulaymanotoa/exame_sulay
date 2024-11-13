from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_Empleado = models.CharField(max_length=20,blank=False,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    puesto = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(null=True)
    def _str_(self):
           return self.nombre
class Puesto_trabajo(models.Model):
    id_puesto = models.CharField(max_length=20, blank=False, primary_key=True)
    nombre_puesto = models.CharField(max_length=100)
    def _str_(self):
            return self.nombre_puesto
class Historial_trabajo(models.Model):
    id_historial = models.CharField(max_length=20, blank=False, primary_key=True)
    id_Empleado = models.ForeignKey(Empleado, on_delete=models.RESTRICT)
    id_puesto = models.ForeignKey(Puesto_trabajo, on_delete=models.RESTRICT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    def _str_(self):
            return self.id_historial
class Contrato (models.Model):
    id_contrato = models.CharField(max_length=20, blank=False, primary_key=True)
    id_Empleado = models.ForeignKey(Historial_trabajo, on_delete=models.RESTRICT)
    id_puesto  = models.ForeignKey(Puesto_trabajo, on_delete=models.RESTRICT) 
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    def _str_(self):
           return self.id_contrato