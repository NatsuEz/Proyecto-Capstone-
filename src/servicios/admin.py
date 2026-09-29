from django.contrib import admin
from .models import Cliente, Plan, Contratacion, DocumentoContrato

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'razon_social', 'tipo_persona', 'email', 'telefono', 'ejecutivo_responsable')
    search_fields = ('rut', 'razon_social', 'email', 'rep_legal_rut')
    list_filter = ('tipo_persona', 'region', 'ejecutivo_responsable')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_servicio', 'precio_mensual', 'precio_anual', 'activo')
    list_filter = ('tipo_servicio', 'activo')
    search_fields = ('nombre', 'descripcion')


@admin.register(Contratacion)
class ContratacionAdmin(admin.ModelAdmin):
    list_display = ('folio', 'cliente', 'plan', 'estado', 'fecha_inicio', 'fecha_vencimiento', 'monto_pagado')
    list_filter = ('estado', 'fecha_inicio', 'fecha_vencimiento')
    search_fields = ('folio', 'cliente__rut', 'cliente__razon_social', 'transaccion_id')


@admin.register(DocumentoContrato)
class DocumentoContratoAdmin(admin.ModelAdmin):
    list_display = ('contratacion', 'tipo_documento', 'estado_firma', 'fecha_firma')
    list_filter = ('estado_firma',)
    search_fields = ('contratacion__folio', 'id_proceso_firma')