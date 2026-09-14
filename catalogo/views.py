from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'catalogo/inicio.html')

def vista_detalle(request):
    return render(request, 'catalogo/detalle.html')