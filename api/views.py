from rest_framework import generics

from . import models
from . import serializers

class ClientListView(generics.ListAPIView):
    # queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects.all()

class EmployeeListView(generics.ListAPIView):
    # queryset = models.Client.objects.all()
    serializer_class = serializers.EmployeeSerializer

    def get_queryset(self):
        return models.Employee.objects.all()
