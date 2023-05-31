from django.db import models

class Cliente(models.Model):
    nombre =            models.CharField(max_length=20)
    apellido_paterno =  models.CharField(max_length=20)
    apellido_materno =  models.CharField(max_length=20)
    telefono =          models.CharField(max_length=45)
    email =             models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password =          models.CharField(max_length=20)
def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno)

class Genero(models.Model):
    id_genero =         models.AutoField(db_column='idGenero', primary_key=True)
    genero =            models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)

class Vendedor(models.Model):
    rut =               models.CharField(primary_key=True, max_length=10)
    nombre =            models.CharField(max_length=60)
    apellido_paterno =  models.CharField(max_length=60)
    apellido_materno =  models.CharField(max_length=60)
    fecha_nacimiento =  models.DateField(blank=False, null=False)
    id_genero =         models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    img_trabajador =    models.ImageField(upload_to='img')
    telefono =          models.CharField(max_length=45)
    email =             models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password =          models.CharField(max_length=20)
    direccion =         models.CharField(max_length=50, blank=True, null=True)
    activo =            models.IntegerField()
def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)


class Categoria(models.Model):
    id_categoria =      models.AutoField(db_column='idCategoria', primary_key=True)
    categoria =         models.CharField(max_length=30, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)


class Productos(models.Model):
    id_producto =       models.AutoField(primary_key=True)
    titulo =            models.CharField(max_length=60)
    precio =            models.IntegerField(max_length=20)
    img_producto =      models.ImageField(upload_to='img')
    descripcion =       models.CharField(max_length=60)
    stock =             models.IntegerField()
    id_categoria =      models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    
def __str__(self):
        return str(self.id_producto)