from rest_framework import generics
from rest_framework import filters

from place.models import Place
from place.serializer import (
    PlaceListSerializer,
    CreatePlaceSerializer
)


class PlaceListAPIView(generics.ListAPIView):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['tag__name']
    ordering_fields = ['distance']


class CreatePlaceAPIView(generics.CreateAPIView):
    serializer_class = CreatePlaceSerializer
    queryset = Place.objects.all()
