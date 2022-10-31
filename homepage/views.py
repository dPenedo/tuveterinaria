from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from productos.models import Producto
from django.views.generic import View
import datetime
import homepage


def index(request):
    params = {}
    params['nombre_sitio'] = 'tuVeterinaria'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto


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
        params["fecha_de_hoy"]=datetime.datetime.now()
        params["mi_lista"]=[1,2,3,4,5,6,7,8]
        params["row3"]="row3"
        params["mi_lista2"]=[]

        return render(request, self.template, params)
