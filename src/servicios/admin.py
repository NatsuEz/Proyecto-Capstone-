from django.contrib import admin
from .models import PerfilCliente, Plan, Contratacion

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'rut_empresa', 'razon_social', 'telefono')
    search_fields = ('user__username', 'rut_empresa', 'razon_social')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_mensual', 'es_popular')

@admin.register(Contratacion)
class ContratacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'plan', 'estado', 'fecha_inicio', 'monto_pagado')
    list_filter = ('estado', 'fecha_inicio')