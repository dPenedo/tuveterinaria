from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from homepage.models import Producto
import homepage


def index(request):
    params = {}
    params['nombre_sitio'] = 'tuVeterinaria'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto


    return render(request, 'homepage/index.html', params)
# Create your views here.
