from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as django_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json

from .forms import RegistroClienteForm
from .models import Plan, Contratacion, PerfilCliente

def pasarela_view(request):
    planes = Plan.objects.all().order_by('precio_mensual')
    return render(request, 'servicios/pasarela.html', {'planes': planes})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente tras el registro
            return redirect('perfil')
    else:
        form = RegistroClienteForm()
    return render(request, 'servicios/registro.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('perfil')

    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
        else:
            error_message = "Usuario o contraseña incorrectos."
    else:
        form = AuthenticationForm()

    return render(request, 'servicios/login.html', {'form': form, 'error_message': error_message})

def perfil_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Si el usuario es TRABAJADOR / EJECUTIVO (is_staff = True)
    if request.user.is_staff:
        todas_contrataciones = Contratacion.objects.all().order_by('-fecha_inicio')
        todos_clientes = PerfilCliente.objects.all()
        
        context = {
            'es_trabajador': True,
            'contrataciones': todas_contrataciones,
            'clientes': todos_clientes,
        }
    else:
        # Si es CLIENTE, solo trae sus contrataciones
        mis_contrataciones = Contratacion.objects.filter(usuario=request.user).order_by('-fecha_inicio')
        context = {
            'es_trabajador': False,
            'contrataciones': mis_contrataciones,
        }

    return render(request, 'servicios/perfil.html', context)

def logout_view(request):
    django_logout(request)
    return redirect('pasarela')

@login_required
@require_POST
def procesar_pago_view(request):
    try:
        data = json.loads(request.body)
        plan_nombre = data.get('plan_nombre')
        
        plan = Plan.objects.get(nombre=plan_nombre)
        
        # Registrar la contratación en la Base de Datos
        contratacion = Contratacion.objects.create(
            usuario=request.user,
            plan=plan,
            monto_pagado=plan.precio_mensual,
            estado='ACTIVO'
        )
        
        return JsonResponse({
            'status': 'success',
            'mensaje': 'Contratación realizada exitosamente',
            'contratacion_id': contratacion.id
        })
    except Plan.DoesNotExist:
        return JsonResponse({'status': 'error', 'mensaje': 'El plan seleccionado no existe en el sistema.'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'mensaje': str(e)}, status=500)