# Generated by Django 2.2.3 on 2019-07-21 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ingredientes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_insumo', models.FloatField()),
                ('ingrediente_insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendientes.Ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_unidad', models.CharField(max_length=100)),
                ('siglas_unidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_receta', models.CharField(max_length=100)),
                ('porciones', models.IntegerField(blank=True, null=True)),
                ('insumos', models.ManyToManyField(to='pendientes.Insumo')),
            ],
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendientes.Unidad'),
        ),
    ]
