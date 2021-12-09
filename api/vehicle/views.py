from rest_framework import generics
from .serializers import VehicleDetailSerializer
from .models import Vehicle


class VehicleCreateView(generics.CreateAPIView):
    serializer_class = VehicleDetailSerializer


class VehicleListView(generics.ListAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()
