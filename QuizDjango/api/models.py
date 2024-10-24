from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator
from django.utils import timezone

class Cliente(models.Model):
    Nombre= models.CharField(max_length=100)
    Apellido= models.CharField(max_length=100)
    Email= models.CharField(max_length=100, unique=True)
    Telefono=models.IntegerField(unique=True)
    Fecha_registro= models.DateField()
    
    def Espacios_vacios(self):
       if  not self.Nombre.strip() or not self.Apellido.strip() or not self.Email.strip() or not str(self.Telefono).strip() or not str(self.Fecha_registro).strip():
        raise ValidationError('No deben haber espacios vacios')
           
    def __str__(self):
        return self.Nombre, self.Apellido, self.Email, self.Telefono, self.Fecha_registro
    
    
class Habitacion(models.Model):
    Precio= models.IntegerField()
    Descripcion= models.CharField(max_length=100)
    
    def clean(self):
        if self.Precio == 0:
           raise ValidationError('El precio debe ser mayor a 0')
       
    def __str__(self):
        return self.Precio, self.Descripcion

class Reserva(models.Model):
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Habitacion= models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    Fecha_entrada= models.DateField()
    Fecha_salida= models.DateField()
    
    def clean(self):
        if self.Fecha_entrada>= self.Fecha_salida:
            raise ValidationError('La fecha de entrada debe ser anterior a la fecha de la salida')
        
        if self.Fecha_entrada < timezone.now().date:
            raise ValidationError('La fecha de entrada no puede ser del pasado')
    
    def __str__(self):
        return str(self.Fecha_entrada), str(self.Fecha_salida)

  
class Pago(models.Model):
    Factura= models.DecimalField(max_digits=10, decimal_places=2)
    Reserva= models.ForeignKey(Reserva, on_delete=models.CASCADE, unique=True)
    Forma_de_pago= models.CharField(max_length=100)
    Monto_total= models.DecimalField(max_digits=10, decimal_places=2)
    
    def clean(self):
        if self.Factura > 0:
            raise ValidationError('La factura debe ser mayo a 0')
        if self.Monto_total > 0:
            raise ValidationError('El monto de la factura debe ser mayor a ')

    def __str__(self):
        return self.Factura, self.Reserva, self.Forma_de_pago, self.Monto_total
    
    
