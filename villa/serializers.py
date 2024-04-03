from rest_framework import serializers

from villa.models import Block, Floor, Apartment


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


class FloorDetailSerializer(serializers.ModelSerializer):
    apartments = serializers.SerializerMethodField()
    class Meta:
        model = Floor
        fields = '__all__'

    def get_apartments(self, obj):
        request = self.context.get('request')
        if request.query_params.get('apartment_number'):
            apartments = obj.apartments.filter(number=request.query_params.get('apartment_number'))
        else:
            apartments = obj.apartments.all()
        serializer = ApartmentSerializer(apartments, many=True, context={'request': request})
        return serializer.data