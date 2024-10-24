from django.urls import path
from . import views

urlpatterns = [
    
    path('clientes/', views.ClienteListCreate.as_view(), name='cliente-list'),
    path('clientes/<int:pk>', views.ClienteDetail.as_view(), name='cliente-detail'),
    
    path('habitaciones/', views.HabitacionListCreate.as_view(), name='habitacion-list'),
    path('habitaciones/<int:pk>', views.HabitacionDetail.as_view(), name='habitacion-detail'),
    
    path('reservas/', views.ReservaListCreate.as_view(), name='reserva-list'),
    path('reservas/<int:pk>', views.ReservaDetail.as_view(), name='reserva-detail'),
    
    path('pago/', views.PagoListCreate.as_view(), name='pago-list'),
    path('pago/<int:pk>', views.PagoDetail.as_view(), name='pago-detail')
]