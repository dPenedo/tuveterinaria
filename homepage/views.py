from django.shortcuts import render
from django.http import HttpResponse

import homepage


def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros online'
    return render(request, 'homepage/index.html', params)
# Create your views here.
