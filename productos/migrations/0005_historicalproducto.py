# Generated by Django 4.1.3 on 2023-02-27 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0004_remove_producto_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProducto',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado'), ('Retirado', 'Retirado')], default='Borrador', max_length=10)),
                ('producto', models.CharField(max_length=150)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha de publicación')),
                ('imagen', models.TextField(blank=True, max_length=100, null=True)),
                ('accesorios', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=0)),
                ('descripcion', models.TextField(default='')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('descuento', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('categoria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='productos.categoria')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical producto',
                'verbose_name_plural': 'historical productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
