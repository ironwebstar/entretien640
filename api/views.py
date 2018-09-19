import json
from django.http import Http404, HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_auth.views import LoginView
from rest_framework.response import Response

from . import models
from . import serializers

class ClientListView(APIView):
    serializer_class = serializers.ClientSerializer
    def get_object(self, pk):
        try:
            return models.Client.objects.get(pk=pk)
        except models.Client.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        clients = models.Client.objects.all()
        serializer = self.serializer_class(clients, context={'request':request}, many=True)
        data = {obj['id']: obj for obj in serializer.data}
        return Response({'success': True, 'data' : data })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(APIView):
    # queryset = models.Client.objects.all()
    serializer_class = serializers.EmployeeSerializer

    def get(self, request, format=None):
        employees = models.Employee.objects.all()
        serializer = self.serializer_class(employees, context={'request':request}, many=True)
        data = {obj['id']: obj for obj in serializer.data}
        return Response({'success': True, 'data' : data })

class CustomLoginView(LoginView):
    # def post(self, request, *args, **kwargs):
    #     is_super = models.CustomUser.is_superuser

    def get_response(self):

        original_repsonse = super().get_response()
        login_user = models.CustomUser.objects.get(email=self.user)
        is_super = login_user.is_superuser

        if is_super:
            mydata = {
                'success' : True,
            }
            original_repsonse.data.update(mydata)
            return original_repsonse
        else:
            mydata = {
                'success' : False,
                'data'    : 'not allowed admin'
            }
            return Response (
                mydata,
                content_type='Content-Type, application/javascript; charset=utf8',
                status=200
            )