# Quiz4Django
Proyecto: Sistema de Hoteles

Este proyecto es un sistema de gestión de reservas que permite a los clientes registrar su información, realizar reservas de habitaciones y gestionar pagos.
Estructura del Proyecto

El sistema está construido utilizando Django y se compone de los siguientes modelos:

    Cliente: Representa a los clientes que realizan reservas.
        Campos:
            Nombre: Nombre del cliente.
            Apellido: Apellido del cliente.
            Email: Correo electrónico único del cliente.
            Telefono: Teléfono único del cliente.
            Fecha_registro: Fecha de registro del cliente.
        Validaciones:
            No debe haber espacios vacíos en los campos.

    Habitacion: Representa las habitaciones disponibles para reservar.
        Campos:
            Precio: Precio de la habitación.
            Descripcion: Descripción de la habitación.
        Validaciones:
            El precio debe ser mayor a 0.

    Reserva: Representa una reserva de habitación realizada por un cliente.
        Campos:
            Cliente: Relación con el modelo Cliente.
            Habitacion: Relación con el modelo Habitacion.
            Fecha_entrada: Fecha de entrada a la habitación.
            Fecha_salida: Fecha de salida de la habitación.
        Validaciones:
            La fecha de entrada debe ser anterior a la fecha de salida.
            La fecha de entrada no puede ser del pasado.

    Pago: Representa un pago asociado a una reserva.
        Campos:
            Factura: Número de factura.
            Reserva: Relación con el modelo Reserva (única).
            Forma_de_pago: Forma de pago utilizada.
            Monto_total: Monto total del pago.
        Validaciones:
            La factura y el monto total deben ser mayores a 0.

Comandos utilizados 

python -m ensurepip --upgrade
py -m pip install Django==5.1.2

python -m django --version
py -m django startproject Django_Test
pip install djangorestframework

para imigrar una tabla
python manage.py migrate api

para crear las migraciones;
python manage.py makemigrations

Aplico la migraciones;
python manage.py migrate

Para correr el servidor
python manage.py runserver