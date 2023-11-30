from django.contrib import admin
from django.urls import path, include
from . import views
from contacto.views import ContactView, PlayListView

urlpatterns = [
    path('contactform/', ContactView.as_view(), name='contactform'),
    path('', PlayListView.as_view(), name='bienvenido')

]
