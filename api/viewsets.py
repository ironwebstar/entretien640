from rest_framework import viewsets, filters
from rest_framework.response import Response

from . import models, serializers

class EmployeeViewSet(viewsets.ModelViewSet):
    __basic_fields = ('first_name', 'last_name', )
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = __basic_fields

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'data': serializer.data})

class ClientViewSet(viewsets.ModelViewSet):
    __basic_fields = ('first_name', 'last_name',)
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = __basic_fields

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'data': serializer.data})

class ProspectViewSet(viewsets.ModelViewSet):
    __basic_fields = ('first_name', 'last_name',)
    queryset = models.Prospect.objects.all()
    serializer_class = serializers.ProspectSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = __basic_fields

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'data': serializer.data})