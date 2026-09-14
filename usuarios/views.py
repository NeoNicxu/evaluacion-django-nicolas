from django.shortcuts import render

def vista_perfil(request):
    return render(request, 'usuarios/perfil.html')

def vista_registro(request):
    return render(request, 'usuarios/registro.html')