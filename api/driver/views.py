from rest_framework import generics, viewsets
from .serializers import DriverDetailSerializer
from .models import Driver


class DriverCreateView(viewsets.ModelViewSet):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()

