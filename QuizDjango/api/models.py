from django.db import models

class Cliente(models.Model):
    Nombre= models.CharField(max_length=100)
    Apellido= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Telefono=models.IntegerField()
    Fecha_registro= models.DateField()
    def __str__(self):
        return self.Nombre, self.Apellido, self.Email, self.Telefono, self.Fecha_registro
    
    
class Habitacion(models.Model):
    Precio= models.DecimalField(max_digits=10, decimal_places=2)
    Descripcion= models.CharField(max_length=100)
    def __str__(self):
        return self.Precio, self.Descripcion

class Reserva(models.Model):
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE, unique=True)
    Habitacion= models.ForeignKey(Habitacion, on_delete=models.CASCADE, unique=True)
    Fecha_entrada= models.DateField()
    Fecha_salida= models.DateField()
    def __str__(self):
        return self.Cliente.Nombre,self.Cliente.Apellido, self.Habitacion, self.Fecha_entrada,self.Fecha_salida
  
class Pago(models.Model):
    Factura= models.DecimalField(max_digits=10, decimal_places=2)
    Reserva= models.ForeignKey(Reserva, on_delete=models.CASCADE, unique=True)
    Forma_de_pago= models.CharField(100)
    Monto_total= models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.Factura, self.Reserva, self.Forma_de_pago, self.Monto_total
    
    
