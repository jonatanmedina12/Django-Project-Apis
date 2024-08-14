#from django.http import JsonResponse
#from django.shortcuts import render
#from .models import Inmueble
#
#
## Create your views here.
#def inmuebles_list(request):
#    inmuebles = Inmueble.objects.all()
#    data = {
#        'inmuebles': list(inmuebles.values())
#    }
#    return JsonResponse(data)
#
#
#def inmueble_detalle(request, pk):
#    inmuebles = Inmueble.objects.get(pk=pk)
#    data ={
#        'direccion':inmuebles.direccion,
#        'pais':inmuebles.pais,
#        'imagen':inmuebles.imagen,
#        'active':inmuebles.active,
#        'descripcion':inmuebles.descripcion
#
#    }
#    return JsonResponse(data)
#