from django.db import models

# Create your models here.
class Portafolio(models.Model):
    portafolio= models.CharField(max_length=20)
    imagen=models.ImageField(upload_to='portafolio',null=True, blank=True)
    tipo=models.CharField(max_length=20, null=True)
    ruta = models.CharField(max_length=200, null= True, blank=True)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.portafolio)

#------------Para vista Acerca de mi----------------
class Trabajo(models.Model):
    trabajo= models.CharField(max_length=20)
    descripcion= models.TextField(max_length=500)
    icono = models.ImageField(upload_to='icono', null=True, blank=True)
    estado=models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.trabajo)

class Acerca(models.Model):
    acerca= models.TextField(max_length=200)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.acerca)

#------------Para vista Resumen----------------
class Certificado(models.Model):
    certificado = models.CharField(max_length=100)
    epoca= models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='certificado', null=True, blank=True)
    descripcion = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.certificado)

class Conocimiento(models.Model):
    conocimiento=models.CharField(max_length=20)
    estado=models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.conocimiento)

class Lenguaje(models.Model):
    lenguaje= models.CharField(max_length=20)
    nivel= models.IntegerField()
    estado= models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.lenguaje)

class Habilidad(models.Model):
    habilidad=models.CharField(max_length=200)
    nivel= models.IntegerField()
    estado= models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.habilidad)

class Experiencia(models.Model):
    cargo=models.CharField(max_length=200)
    lugar=models.CharField(max_length=20)
    epoca=models.CharField(max_length=10)
    descripcion=models.TextField(max_length=200)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.cargo)  

class Educacion(models.Model):
    educacion= models.CharField(max_length=100)
    epoca=models.IntegerField()
    colegio= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=200)
    estado= models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.educacion)
#------------------------------------------------

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    paterno = models.CharField(max_length=200)    
    materno = models.CharField(max_length=200)    
    direccion=models.CharField(max_length=200)
    correo= models.EmailField(max_length=200)
    telefono=models.CharField(max_length=50)
    profesion=models.CharField(max_length=200)
    foto = models.ImageField(upload_to='foto', null=True, blank=True)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    estado=models.BooleanField(default=True)
    curriculum = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nombre)  

