from django.urls import path

from .views import inmuebles_list,inmueble_detalle

urlpatterns = [
    path('list', inmuebles_list, name='inmuebles_list'),
    path('<int:pk>',inmueble_detalle,name='inmueble_detalle')
]
