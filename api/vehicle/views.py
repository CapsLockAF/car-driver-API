from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vehicle
from .serializers import VehicleDetailSerializer, SetDriverSerializer


@api_view(['GET', 'POST'])
def vehicles_list(request):
    """
    List all vehicles, vehicles with drives and without them,
     or create a new vehicle.
    """

    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        if request.GET and request.GET['with_drivers'] == 'yes':
            vehicles = Vehicle.objects.exclude(driver_id__isnull=True)
        if request.GET and request.GET['with_drivers'] == 'no':
            vehicles = Vehicle.objects.exclude(driver_id__isnull=False)
        serializer = VehicleDetailSerializer(vehicles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VehicleDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()


class SetDriverView(viewsets.ModelViewSet):
    serializer_class = SetDriverSerializer
    queryset = Vehicle.objects.all()

    def set_driver(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response({"detail": "The vehicle does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = SetDriverSerializer(vehicle, data=request.data)
        serializer_class = VehicleDetailSerializer(vehicle)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer_class.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
