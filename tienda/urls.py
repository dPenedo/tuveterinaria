from django.urls import path
from tienda import views
from tienda import views_agregar
from tienda.views import VerImagenesAlimentos
from tienda.views import VerImagenesAccesorios
from tienda.views import VerImagenesFarmacia
from tienda.views import ver_imagenFarmacia
from tienda.views import ver_imagenAlimentos
from tienda.views import ver_imagenAccesorios
from tienda.views import EjemploLocalSotage

urlpatterns = [
        path('cargar/', views.cargar_imagen, name="cargar"),
        path('<int:producto_id>/ver-alimentos/', views.ver_imagenAlimentos, name="verAlimentos"),
        path('<int:producto_id>/ver-accesorios/', views.ver_imagenAccesorios, name="verAccesorios"),
        path('<int:producto_id>/ver-farmacia/', views.ver_imagenFarmacia, name="verFarmacia"),
        path('alimentos/', VerImagenesAlimentos.as_view(), name="alimentos"),
        path('accesorios/', VerImagenesAccesorios.as_view(), name="accesorios"),
        path('farmacia/', VerImagenesFarmacia.as_view(), name="farmacia"),
        path('ejemplo_localstorage/', EjemploLocalSotage.as_view(), name="ejemplo_localstorage"),
        path('agregar/', views_agregar.agregar, name="agregar"),

        ]
