# Generated by Django 3.1.2 on 2020-11-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0009_auto_20201110_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='tipo_indi',
            field=models.CharField(choices=[('Indicador de Eficiencia', 'Indicador de Eficiencia'), ('Indicador de Eficacia', 'Indicador de Eficacia'), ('Indicador de Economía', 'Indicador de Economía'), ('Indicador de Producto', 'Indicador de Producto'), ('Indicador de Resultado', 'Indicador de Resultado'), ('Indicador de Insumo', 'Indicador de Insumo'), ('Indicador de Calidad', 'Indicador de Calidad'), ('Indicador de Proceso', 'Indicador de Proceso')], default='Indicador de Eficiencia', max_length=30),
        ),
    ]
