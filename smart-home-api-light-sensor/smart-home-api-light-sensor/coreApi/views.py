from django.http.response import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from coreApi.models import Device as DeviceModel
from coreApi.serializers import DeviceSerializer
from coreApi.utils import *

# Create your views here.
class Devices(APIView):
    def get(self, request, format=None):
        devices = DeviceModel.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Device(APIView):
    def get_object(self, pk):
        try:
            return DeviceModel.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            setPinStatus(int(serializer.data.get('id')),
                         serializer.data.get('status'))
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        device = self.get_object(pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResetPin(APIView):
    def post(self, request, pk, format=None):
        resetPinStatus(int(pk))
        return Response(status=status.HTTP_200_OK)

    def get(self, request, format=None):
        devices = DeviceModel.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        for device in serializer.data:
            setupPin(int(device['id']))
            print(device['id'])
        return Response(serializer.data)
