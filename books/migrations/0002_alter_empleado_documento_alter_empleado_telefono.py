# Generated by Django 4.2.3 on 2023-07-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado", name="documento", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="empleado", name="telefono", field=models.IntegerField(),
        ),
    ]
