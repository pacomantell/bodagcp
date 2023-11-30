from django.http import HttpResponse
from django.shortcuts import render


def datosEvento(request):
    return render(request, 'datos_evento.HTML', {'nbar': 'datos_evento'})


def not_found(request, exception):
    return render(request, 'admin/404.html', status=404)
