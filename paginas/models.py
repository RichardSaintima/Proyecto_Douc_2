from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.auth.models import User

class Genero(models.Model):
    id_genero =         models.AutoField(db_column='idGenero', primary_key=True)
    genero =            models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('El email debe ser proporcionado')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email



class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    is_vendedor = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.user.username}'


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




