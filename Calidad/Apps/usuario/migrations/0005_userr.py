# Generated by Django 3.1.2 on 2020-11-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_model_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
