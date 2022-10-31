from django.urls import path
from homepage import views
from homepage.views import Templatetags1

urlpatterns = [
    path('', views.index, name='index'),
    path('templatetags1', Templatetags1.as_view(), name="templatetags1"),

]
