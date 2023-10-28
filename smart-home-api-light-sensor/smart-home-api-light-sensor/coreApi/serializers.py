from rest_framework import serializers
from .models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'status']
    # id = serializers.CharField()
    # name = serializers.CharField()
    # status = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Device.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance
