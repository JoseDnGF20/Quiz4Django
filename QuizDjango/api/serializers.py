from rest_framework import serializers
from .models import Cliente, Habitacion, Reserva, Pago

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        field = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        field = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        field = '__all__'


