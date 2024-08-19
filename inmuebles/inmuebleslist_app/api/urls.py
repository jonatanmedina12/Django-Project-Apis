from django.urls import path

from .views import InmueblesListAv, InmueblesDetalleAv, EmpresasAv, EmpresasDetalleAv

urlpatterns = [
    path('inmuebles/', InmueblesListAv.as_view(), name='inmueble-list'),
    path('inmuebles/<int:pk>/', InmueblesDetalleAv.as_view(), name='inmueble-detalle'),
    path('empresas/', EmpresasAv.as_view(), name='empresa-list'),
    path('empresas/<int:pk>/', EmpresasDetalleAv.as_view(), name='empresa-detalle'),

]