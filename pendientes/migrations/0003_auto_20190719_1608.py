# Generated by Django 2.2.3 on 2019-07-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendientes', '0002_recetas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientes', models.CharField(max_length=100)),
                ('porcion', models.CharField(max_length=100)),
                ('produccion', models.CharField(max_length=100)),
                ('precios', models.CharField(max_length=100)),
                ('costo_total', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Recetas',
        ),
    ]