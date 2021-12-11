from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vehicle
from .serializers import VehicleDetailSerializer, SetDriverSerializer


@api_view(['GET', 'POST'])
def vehicles_list(request):
    """
    List of all vehicles, vehicles with drives and without them,
     or create a new vehicle.
     create vehicle POST {
        "make": "str",
        "model": "str",
        "plate_number": "AA 2255 BB" - unique
    }
    Filter vehicles by driver:
        /?with_drivers=yes or /?with_drivers=no
    """
    # filter vehicles by vehicle with driver
    if request.method == 'GET':
        if request.GET.get('with_drivers'):
            flag = request.GET.get('with_drivers') == 'yes'
            vehicles = Vehicle.objects.exclude(driver_id__isnull=flag)
        else:
            vehicles = Vehicle.objects.all()
        serializer = VehicleDetailSerializer(vehicles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # create a vehicle
        serializer = VehicleDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Provides get, put, patch and delete method handlers for Vehicle"""
    serializer_class = VehicleDetailSerializer
    queryset = Vehicle.objects.all()


class SetDriverView(viewsets.ModelViewSet):
    """put the driver in the car / get the driver out of the car.
    Only POST {
            "driver_id": null or int:driver_id
        }"""
    serializer_class = SetDriverSerializer
    queryset = Vehicle.objects.all()

    def set_driver(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response({"id": {"detail": "The vehicle does not exist. Wrong ID"} },
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = SetDriverSerializer(vehicle, data=request.data)
        serializer_vehicles = VehicleDetailSerializer(vehicle)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer_vehicles.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
