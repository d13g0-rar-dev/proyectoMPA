# Generated by Django 4.2.3 on 2023-07-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0008_remove_ciudad_id_alter_ciudad_nombre_ciudad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ciudad",
            name="nombre_ciudad",
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="empresa",
            name="nombre_empresa",
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="tipodocumento",
            name="nombre_tipo",
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]