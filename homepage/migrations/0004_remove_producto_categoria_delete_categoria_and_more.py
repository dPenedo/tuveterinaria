# Generated by Django 4.1.1 on 2022-10-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_categoria_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]