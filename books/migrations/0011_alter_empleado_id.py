# Generated by Django 4.2.3 on 2023-07-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0010_alter_empleado_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="id",
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]