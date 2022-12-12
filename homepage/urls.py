from django.urls import path
from homepage import views
from homepage.views import Templatetags1
from homepage.views import BuscarLibro

urlpatterns = [
    path('', views.index, name='index'),
    path('templatetags1', Templatetags1.as_view(), name="templatetags1"),
    path('usar_ajax', views.para_ajax, name='usar_ajax'),
    path('buscar_libro/', BuscarLibro.as_view(), name="buscar_libro"),

]
