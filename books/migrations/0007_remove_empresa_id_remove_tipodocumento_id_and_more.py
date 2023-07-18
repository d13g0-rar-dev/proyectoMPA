# Generated by Django 4.2.3 on 2023-07-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_remove_ciudad_descripcion_ciudad_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="empresa", name="id",),
        migrations.RemoveField(model_name="tipodocumento", name="id",),
        migrations.AlterField(
            model_name="empresa",
            name="nombre_empresa",
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="tipodocumento",
            name="nombre_tipo",
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
