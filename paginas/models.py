from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Genero(models.Model):
    id_genero =         models.AutoField(db_column='idGenero', primary_key=True)
    genero =            models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)
    is_vendedor = models.BooleanField(default=False)
   
#    Para Hashar Password

    # def save(self, *args, **kwargs):
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.is_vendedor}'


class Categoria(models.Model):
    id_categoria =      models.AutoField(db_column='idCategoria', primary_key=True)
    categoria =         models.CharField(max_length=30, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)


class Producto(models.Model):
    id_producto =       models.AutoField(primary_key=True)
    titulo =            models.CharField(max_length=60)
    precio =            models.IntegerField()
    imagen =            models.ImageField (upload_to='img', null=True, blank=True)
    descripcion =       models.CharField(max_length=210)
    id_categoria =      models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    
def __str__(self):
        return str(self.titulo)+" "+str(self.id_producto)




