# from datetime import datetime
# from http.client import HTTPResponse
# import mimetypes

from django.http.response import mimetypes
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from productos.models import Producto
from django.views.generic import View
import datetime
from django.shortcuts import redirect
import homepage
import json
from django.http import HttpResponse
from productos.forms import SearchLibroForm


def para_ajax(request):
    params = {}
    search =  SearchLibroForm()
    params['search'] = search
    return render(request, 'homepage/ver_ajax.html', params)

class BuscarLibro(View):
    def get(self, request):
        if request.is_ajax:
            palabra = request.GET.get('term', '')
            print(palabra)
            libro = Producto.objects.filter(producto__icontains = palabra)
            result = []
            for an in libro:
                data = {}
                data['label'] = an.producto
                result.append(data)
            data_json = json.dumps(result)
        else:
            data_json = "Falló"
        mimetype = "application/json"
        return HttpResponse (data_json, mimetype)


def index(request):
    params = {}
    params['nombre_sitio'] = 'tuVeterinaria'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto'] = producto


    return render(request, 'homepage/index.html', params)



class Templatetags1(View):
    template = "homepage/templatetags1.html"
    def get(self, request):
        params = {}
        params["cross_site_scripting"]="""
            <script>
            $("*").css({
                "background-color": "yellow",
                "font-weight": "bolder",
                "margin-bottom": "200px",
            });
            </script>
        
        """
        producto = Producto.objects.filter( Q(estado="Publicado"), )
        params["los_productos"] = producto
        params["fecha_de_hoy"] = datetime.datetime.now()
        params["mi_lista"] = [1,2,3,4,5,6,7,8]
        params["row3"] = "row3"
        params["mi_lista2"] = []

        return render(request, self.template, params)
    def post(self, request):
        params = {}
        producto=request.POST.get("producto")
        el_pedido = request.session.get("el_pedido")
        if el_pedido:
            cantidad = el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]=cantidad+1
            else:
                el_pedido[producto]=1
        else:
            el_pedido = {}
            el_pedido[producto] = 1

        request.session["el_pedido"] = el_pedido
        print(request.session["el_pedido"])

        return redirect("templatetags1")
