from django.urls import path
from . import views

urlpatterns = [
    path('', views.pasarela_view, name='pasarela'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('procesar-pago/', views.procesar_pago_view, name='procesar_pago'),
]