from django.contrib.auth.hashers import make_password
from rest_framework import permissions
from django.db.models import Q
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from . import models
from . import serializers


class CustomLoginView(LoginView):

    def get_response(self):
        original_repsonse = super().get_response()
        login_user = models.CustomUser.objects.get(email=self.user)
        is_super = login_user.is_superuser
        if is_super:
            mydata = {'success': True}
            original_repsonse.data.update(mydata)
            return original_repsonse
        else:
            mydata = {'success': False, 'data': 'not allowed admin'}
            return Response(
                mydata,
                content_type='Content-Type, application/javascript; charset=utf8',
                status=200
            )

class ProspectListView(APIView):
    serializer_class = serializers.ProspectSerializer

    def get(self, request):
        prospects = models.Prospect.objects.all()
        serializer = self.serializer_class(prospects, context={'request': request}, many=True)
        return Response({'success': True, 'data': serializer.data})

class ClientListView(ListAPIView):
    serializer_class = serializers.ClientSerializer
    def get(self, request, *args, **kwargs):
        clients = models.Client.objects.all()
        serializer = self.serializer_class(clients, context={'request': request}, many=True)
        return Response({'success': True, 'data': serializer.data})

class ClientCreateView(APIView):
    def post(self, request, format=None):
        data = request.data
        assign_employee = models.Employee.objects.get(id=data['assign_to'])
        if models.Client.objects.filter(username=data['username']):
            data = 'existed_username'
            return Response({'success': False, 'data':data})
        if models.Client.objects.filter(email=data['email']):
            data = 'existed_email'
            return Response({'success': False, 'data': data})

        new_client = models.Client.objects.create(username=data['username'], password=data['password'],
                                                  email=data['email'], assign_to=assign_employee,
                                                  profit_month=data['profit_month'])
        new_client.save()
        return Response({'success': True})

class ClientEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        return models.Client.objects.filter(id=self.request.id)

    def get_object(self):
        return get_object_or_404(models.Client, pk=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        original = self.retrieve(request, *args, **kwargs).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        original = Response(serializer.data).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def delete(self, request, *args, **kwargs):
        original = self.destroy(request, *args, **kwargs).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def get(self, request):
        data = request.data
        cond_1 = Q(first_name_contains=data['string'])
        cond_2 = Q(last_name_contains=data['string'])
        employees = models.Employee.objects.filter(cond_1 | cond_2)
        return Response({'success':True, 'data': employees})

class EmployeeListView(APIView):
    serializer_class = serializers.EmployeeSerializer

    def get(self, request):
        employees = models.Employee.objects.all()
        serializer = self.serializer_class(employees, context={'request': request}, many=True)
        return Response({'success': True, 'data': serializer.data})

class EmployeeCreateView(APIView):
    def post(self, request):
        data = request.data
        if models.Employee.objects.filter(username=data['username']):
            data = 'existed_username'
            return Response({'success': False, 'data':data})
        if models.Employee.objects.filter(email=data['email']):
            data = 'existed_email'
            return Response({'success': False, 'data': data})

        new_employee = models.Employee.objects.create(username=data['username'],
                                                      password=make_password(data['password']),
                                                      email=data['email'], position=data['position'],
                                                      Supervisor=data['Supervisor'], note=data['note'])
        new_employee.save()
        return Response({'success': True})

class EmployeeEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.EmployeeSerializer

    def get_queryset(self):
        return models.Employee.objects.filter(id=self.request.id)

    def get_object(self):
        return get_object_or_404(models.Employee, pk=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        original = self.retrieve(request, *args, **kwargs).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        original = Response(serializer.data).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def delete(self, request, *args, **kwargs):
        original = self.destroy(request, *args, **kwargs).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})