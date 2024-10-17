from django.db import models

# Create your models here.

class AlumnoT(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno"),
    amaterno=models.CharField(max_length=50,verbose_name="Apellido paterno"),
    nombre=models.CharField(max_length=50,verbose_name="Apellido paterno"),
    fehca_nacimiento=models.DateField(verbose_name="Fecha nacimiento",null=False,blank=False),
    fehca_ingreso=models.DateField(verbose_name="Fecha ingreso",null=False,blank=False),


    class Meta:
        db_table="Alumnos"
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"

class Frase(models.Model):
    comentario=models.TextField(verbose_name="Comentario",max_length=400),
    Alumno_fk=models.ForeignKey(AlumnoT,on_delete=models.CASCADE),


    class Meta:
        verbose_name="Frase"
        verbose_name_plural="frases"