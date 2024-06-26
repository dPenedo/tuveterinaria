"""tuVeterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.global_settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('homepage.urls')),
    #path('accounts/', include('registration.backends.default.urls')),
    # path('accounts/', include('django_registration.backends.activation.urls')),
    path('tienda/', include('tienda.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
    path('contacto/', include('contacto.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),    

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += path('__debug__', include(debug_toolbar.urls)),
