from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DriverDetailSerializer
from .models import Driver
from datetime import datetime


@api_view(['GET', 'POST'])
def drivers_list(request):
    """
    List of drivers, a filter of car drivers by created date,
     or create a new driver.
     POST {
            "first_name": "str",
            "last_name": "str"
            }
    filter by date GET /?created_at__gte=10-12-2021 or
                    /?created_at__lte=10-12-2021
    """
    if request.method == 'GET':
        if request.query_params.get('created_at__gte'):
            drivers = Driver.objects.filter(
                created_at__gte=datetime.strptime(
                    request.GET['created_at__gte'],
                    '%d-%m-%Y'))
        elif request.query_params.get('created_at__lte'):
            drivers = Driver.objects.filter(
                created_at__lte=datetime.strptime(
                    request.GET['created_at__lte'],
                    '%d-%m-%Y'))
        else:
            drivers = Driver.objects.all()
        serializer = DriverDetailSerializer(drivers, many=True)
        return Response(serializer.data)

    # create a driver object
    elif request.method == 'POST':
        serializer = DriverDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Provides get, put, patch and delete method handlers"""
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()



