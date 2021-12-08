from django.shortcuts import render
from rest_framework import generics
from .serializers import VehicleDetailSerializer


class VehicleCreateView(generics.CreateAPIView):
    serializer_class = VehicleDetailSerializer
