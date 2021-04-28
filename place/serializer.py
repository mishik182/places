from rest_framework import serializers

from place.models import Place


class PlaceListSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Place
        fields = '__all__'


class CreatePlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'
