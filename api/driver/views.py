from rest_framework import generics
from .serializers import DriverDetailSerializer


class DriverCreateView(generics.CreateAPIView):
    serializer_class = DriverDetailSerializer

