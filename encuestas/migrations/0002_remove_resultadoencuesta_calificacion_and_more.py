# Generated by Django 4.0.4 on 2024-06-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultadoencuesta',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='resultadoencuesta',
            name='usuario',
        ),
        migrations.AddField(
            model_name='resultadoencuesta',
            name='respuesta',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='activa',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='texto_encuesta',
            field=models.CharField(max_length=255),
        ),
    ]
