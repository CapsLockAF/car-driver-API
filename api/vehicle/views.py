from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vehicle
from .serializers import VehicleDetailSerializer, SetDriverSerializer


class VehicleCreateView(viewsets.ModelViewSet):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()


class SetDriverView(viewsets.ModelViewSet):
    serializer_class = SetDriverSerializer
    queryset = Vehicle.objects.all()

    def set_driver(self, request, pk):
        try:
            snippet = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response({"detail": "The vehicle does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = SetDriverSerializer(snippet, data=request.data)
        serializer_class = VehicleDetailSerializer(snippet)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer_class.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)







