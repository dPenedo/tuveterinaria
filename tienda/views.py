from django.shortcuts import render
from django.shortcuts import redirect
from productos.models import Producto
from tienda.forms import CargarForm
from django.http import Http404
from django.views.generic import View


def cargar_imagen(request):
    params = {}

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form'] = form
        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            imagen = form.cleaned_data['imagen']

            nuevo_producto = Producto(producto=producto, fecha_publicacion=fecha_publicacion, imagen=imagen)
            nuevo_producto.save()
            return redirect('index')

    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/formulario.html', params)

class VerImagenesAlimentos(View):
    template = "tienda/alimentos.html"
    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        return render(request, self.template, params)

class VerImagenesFarmacia(View):
    template = "tienda/farmacia.html"
    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        return render(request, self.template, params)

class VerImagenesAccesorios(View):
    template = "tienda/accesorios.html"
    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        return render(request, self.template, params)

def ver_imagen(request, producto_id):
    params = {}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    return render(request, "tienda/verimagen.html", params)

def ver_imagenAlimentos(request, producto_id):
    params = {}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    return render(request, "tienda/alimentos.html", params)

def ver_imagenAccesorios(request, producto_id):
    params = {}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    return render(request, "tienda/ver-accesorios.html", params)

def ver_imagenFarmacia(request, producto_id):
    params = {}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    return render(request, "tienda/ver-farmacia.html", params)

class EjemploLocalSotage(View):
    template = "tienda/localstorage.html"

    def get(self, request):
        params = {}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos

        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}

        return render(request, self.template, params)

