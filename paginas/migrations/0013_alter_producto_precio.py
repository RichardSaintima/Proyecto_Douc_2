# Generated by Django 4.2.1 on 2023-06-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0012_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
