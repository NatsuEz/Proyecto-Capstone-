from django.urls import path
from . import views

urlpatterns = [
    path('', views.pasarela_view, name='pasarela'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('procesar-pago/', views.procesar_pago_view, name='procesar_pago'),
    path('comprobante/<int:contratacion_id>/pdf/', views.descargar_comprobante_pdf, name='descargar_comprobante_pdf'),
    path('comprobante/<int:contratacion_id>/pdf/', views.descargar_comprobante_pdf, name='descargar_comprobante'),
    
    # Rutas CRM Ejecutivo
    path('crm/', views.crm_dashboard_view, name='crm_dashboard'),
    path('crm/cambiar-estado/<int:contratacion_id>/', views.cambiar_estado_contratacion, name='cambiar_estado_contratacion'),
]