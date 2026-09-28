from django.db import models
from django.contrib.auth.models import User

# Modelos para la base de datos de Easy Office

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rut_empresa = models.CharField(max_length=12, verbose_name="RUT Empresa/Persona")
    razon_social = models.CharField(max_length=150, blank=True, null=True, verbose_name="Razón Social")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono de Contacto")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección Particular")

    def __str__(self):
        return f"{self.user.username} - {self.rut_empresa}"


class Plan(models.Model):
    nombre = models.CharField(max_length=50)
    precio_mensual = models.IntegerField(help_text="Precio en CLP")
    descripcion = models.TextField(blank=True)
    es_popular = models.BooleanField(default=False, verbose_name="¿Es el plan destacado?")

    def __str__(self):
        return f"{self.nombre} (${self.precio_mensual:,} CLP)"


class Contratacion(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Pago'),
        ('ACTIVO', 'Servicio Activo'),
        ('CANCELADO', 'Cancelado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contrataciones')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    monto_pagado = models.IntegerField()

    def __str__(self):
        return f"Contrato #{self.id} - {self.usuario.username} ({self.plan.nombre})"