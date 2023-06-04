# Generated by Django 4.2.1 on 2023-06-03 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0018_alter_producto_imagen_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido_paterno', models.CharField(max_length=60)),
                ('apellido_materno', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.IntegerField()),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='paginas.genero')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]