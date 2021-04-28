from django.urls import path

from place.views import (
    PlaceListAPIView,
    CreatePlaceAPIView
)

urlpatterns = [
    path('places/', PlaceListAPIView.as_view(), name='place_list'),
    path('place/', CreatePlaceAPIView.as_view(), name='create_place'),
]
