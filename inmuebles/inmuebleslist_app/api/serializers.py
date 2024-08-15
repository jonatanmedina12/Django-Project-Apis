from rest_framework import serializers
from ..models import Inmueble


def column_longitud(value):
    if len(value) < 2:
        raise serializers.ValidationError("la direction es demasiado corta")


class InmueblesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(validators=[column_longitud])
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Inmueble.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('la direccion y el pais deben ser differences')
        else:
            return data

    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("muy corta como la de su papa")
        else:
            return data
