from rest_framework import serializers

from villa.models import Villa, Block, Floor, Apartment


class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'