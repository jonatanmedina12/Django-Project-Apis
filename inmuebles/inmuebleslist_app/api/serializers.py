from rest_framework import serializers

from ..models import Inmueble, Empresa, Comentario


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields ="__all__"

class InmueblesSerializer(serializers.ModelSerializer):
    comentarios =ComentariosSerializer(many=True,read_only=True)

    longitud_direccion = serializers.SerializerMethodField()

    class Meta:
        model = Inmueble
        fields = ['id', 'pais', 'active', 'imagen', 'longitud_direccion', 'direccion']

    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('La dirección y el país deben ser diferentes')
        return data

    def get_longitud_direccion(self, obj):
        return len(obj.direccion)

    @staticmethod
    def validate_imagen(data):
        if len(data) < 2:
            raise serializers.ValidationError("La imagen es demasiado corta")
        return data


class EmpresasSerializer(serializers.ModelSerializer):
    #Empresa_list = InmueblesSerializer(many=True,read_only=True)
    #Empresa_list = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    Empresa_list = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='inmueble-detalle'
    )

    class Meta:
        model = Empresa
        fields = "__all__"

#def column_longitud(value):
#    if len(value) < 2:
#        raise serializers.ValidationError("la direction es demasiado corta")
#
#
#class InmueblesSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    direccion = serializers.CharField(validators=[column_longitud])
#    pais = serializers.CharField()
#    descripcion = serializers.CharField()
#    imagen = serializers.CharField()
#    active = serializers.BooleanField()
#
#    def create(self, validated_data):
#        return Inmueble.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.direccion = validated_data.get('direccion', instance.direccion)
#        instance.pais = validated_data.get('pais', instance.pais)
#        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#        instance.imagen = validated_data.get('imagen', instance.imagen)
#        instance.active = validated_data.get('active', instance.active)
#        instance.save()
#        return instance
#
#    def validate(self, data):
#        if data['direccion'] == data['pais']:
#            raise serializers.ValidationError('la direccion y el pais deben ser differences')
#        else:
#            return data
#
#    def validate_imagen(self, data):
#        if len(data) < 2:
#            raise serializers.ValidationError("muy corta como la de su papa")
#        else:
#            return data
#
