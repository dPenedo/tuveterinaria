from django.urls import path
from homepage import views
from homepage.views import Templatetags1
from homepage.views import BuscarLibro
from homepage.views import BuscarLibro2

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_libro2/', BuscarLibro2.as_view(), name="buscar_libro2"),
    path('buscar_libro/', BuscarLibro.as_view(), name="buscar_libro"),
    path('templatetags1', Templatetags1.as_view(), name="templatetags1"),
    path('usar_ajax', views.para_ajax, name='usar_ajax'),
    path('reserva/', views.nodisponible, name='reserva'),
    path('peluqueria/', views.nodisponible, name='peluqueria'),
]
