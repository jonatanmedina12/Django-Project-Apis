from ..models import Inmueble
from .serializers import InmueblesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def inmueble_list(request):
    if request.method == 'GET':
        inmuebles = Inmueble.objects.all()
        serializer = InmueblesSerializer(inmuebles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        de_serializer = InmueblesSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def inmueble_detalle(request, pk):
    try:
        if request.method == 'GET':
            inmueble = Inmueble.objects.get(pk=pk)

            serializer = InmueblesSerializer(inmueble)
            return Response(serializer.data)
        if request.method == 'PUT':
            inmueble = Inmueble.objects.get(pk=pk)

            de_serializer = InmueblesSerializer(inmueble, data=request.data)
            if de_serializer.is_valid():
                de_serializer.save()
                return Response(de_serializer.data, status=status.HTTP_201_CREATED)
            return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':

            inmueble = Inmueble.objects.get(pk=pk)

            inmueble.delete()
            data={
                "resultado":True
            }

            return Response(data, status=status.HTTP_201_CREATED)


    except Inmueble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
