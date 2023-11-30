"""boda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


from . import views
from ConfirmaAsistente.admin import admin_site

# Admin customization
admin.site.site_header = 'Boda Francisco & Raquel'
admin.site.index_title = 'Administración'
admin.site.site_title = 'Boda F&R'

urlpatterns = [
    path('', include('contacto.urls')),
    path('datos_evento/', views.datosEvento, name='datos_evento'),
    path('admin/', admin.site.urls, name='admin'),
    path('admin-dashboard/', admin_site.urls, name='dashboard'),
    path('confirmacion/', include('ConfirmaAsistente.urls'))

]

handler404 = "boda.views.not_found"
