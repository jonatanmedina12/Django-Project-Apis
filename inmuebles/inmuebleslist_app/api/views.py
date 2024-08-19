
from ..models import Inmueble, Empresa
from .serializers import InmueblesSerializer, EmpresasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class EmpresasAv(APIView):
    @staticmethod
    def get(request):
        empresas = Empresa.objects.all()
        serializer = EmpresasSerializer(empresas, many=True, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = EmpresasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresasDetalleAv(APIView):
    @staticmethod
    def get(request, pk):
        try:
            empresas = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresasSerializer(empresas, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def update(request, pk):
        try:
            empresas = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresasSerializer(empresas, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        try:
            empresas = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        empresas.delete()
        return Response(status=status.HTTP_200_OK)

class InmueblesListAv(APIView):
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmueblesSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = InmueblesSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InmueblesDetalleAv(APIView):
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
            serializer = InmueblesSerializer(inmueble)
            return Response(serializer.data)
        except Inmueble.DoesNotExist:
            return Response(
                {"error": "Inmueble no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        try:
            inmuebles = Inmueble.objects.get(pk=pk)

        except Inmueble.DoesNotExist:
            return Response(
                {"error": "Inmueble no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        inmuebles.delete()
        return Response('correcto', status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            inmuebles = Inmueble.objects.get(pk=pk)

        except Inmueble.DoesNotExist:
            return Response(
                {"error": "Inmueble no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = InmueblesSerializer(inmuebles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('correcto', status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Inmueble no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
