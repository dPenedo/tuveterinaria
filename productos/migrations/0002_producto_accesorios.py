# Generated by Django 4.1.3 on 2023-02-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='accesorios',
            field=models.BooleanField(default=False),
        ),
    ]
