# Generated by Django 4.2.7 on 2023-11-25 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoriaHab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20)),
                ('total_cuartos', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('tipo_cliente', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numhabitacion', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('max_personas', models.IntegerField()),
                ('edificio', models.CharField(max_length=2)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.categoriahab')),
            ],
        ),
        migrations.CreateModel(
            name='tipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
                ('cargoServicio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('cargo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='reservaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('num_personas', models.IntegerField()),
                ('nom_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.cliente')),
                ('numhabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.habitaciones')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.tipopago')),
            ],
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.trabajadores'),
        ),
    ]
