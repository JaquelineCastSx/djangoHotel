from django.db import models

# Create your models here.

class categoriaHab(models.Model):
    categoria = models.CharField(max_length=20)
    total_cuartos = models.IntegerField()
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return f"Categoria: {self.categoria},  Total habitaciones:{self.total_cuartos}"

class trabajadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, posición: {self.cargo}"

class tipoPago(models.Model):
    tipo = models.CharField(max_length=40)
    cargoServicio = models.IntegerField()

    def __str__(self):
        return f"{self.tipo}, cargo: {self.cargoServicio}%"


class cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    tipo_cliente = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.tipo_cliente}"


class habitaciones(models.Model):
    numhabitacion = models.IntegerField()
    precio = models.IntegerField()
    max_personas = models.IntegerField()
    edificio = models.CharField(max_length=2)
    categoria = models.ForeignKey(categoriaHab, on_delete=models.CASCADE)
    encargado = models.ForeignKey(trabajadores, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}- habitacion: {self.numhabitacion}, categoria: {self.categoria}, ${self.precio}, max: {self.max_personas} personas"


class reservaciones(models.Model):
    nom_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    numhabitacion = models.ForeignKey(habitaciones, on_delete=models.CASCADE)
    fechaIngreso = models.DateField()
    fechaSalida = models.DateField()
    num_personas = models.IntegerField()
    pago = models.ForeignKey(tipoPago, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} A nombre de: {self.nom_cliente}, habitacion: {self.numhabitacion}, llegada: {self.fechaIngreso}, salida: {self.fechaSalida}"


