# Generated by Django 5.0.7 on 2024-07-31 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saoapp', '0004_curso_entregable_estudiante_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='comision',
            field=models.IntegerField(),
        ),
    ]