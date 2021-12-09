from rest_framework import generics, views, viewsets
from .serializers import DriverDetailSerializer
from .models import Driver


class DriverCreateView(generics.CreateAPIView):
    serializer_class = DriverDetailSerializer


class DriverListView(generics.ListAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()

