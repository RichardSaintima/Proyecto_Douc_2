# Generated by Django 4.2.1 on 2023-06-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0032_alter_persona_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]