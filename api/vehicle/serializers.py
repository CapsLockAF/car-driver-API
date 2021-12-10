from rest_framework import serializers
from .models import Vehicle


class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class SetDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['driver_id']
