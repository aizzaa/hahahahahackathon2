from rest_framework import viewsets
from .models import Hotels
from rest_framework.response import Response
from .serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer