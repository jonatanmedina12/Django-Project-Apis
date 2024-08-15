from django.urls import path

from .views import InmueblesListAv

from .views import InmueblesDetalleAv

urlpatterns = [
    path('list', InmueblesListAv.as_view(), name='inmuebles_list'),
    path('<int:pk>', InmueblesDetalleAv.as_view(), name='inmueble_detalle')
]
