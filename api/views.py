from django.contrib.auth.hashers import make_password
from rest_framework import permissions, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_auth.views import LoginView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
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

class SmallPagination(PageNumberPagination):
    page_size = 5

class ClientListView(ListAPIView):
    serializer_class = serializers.ClientSerializer
    pagination_class = SmallPagination

    def get(self, request, *args, **kwargs):
        clients = models.Client.objects.all()
        serializer = self.serializer_class(clients, context={'request': request}, many=True)
        page = self.paginate_queryset(serializer.data)
        serializer = self.get_paginated_response(page)
        return Response({'success': True, 'data': serializer.data})



class ClientCreateView(APIView):
    serializer_class = serializers.ClientSerializer
    def post(self, request):
        data = request.data
        try:
            assign_employee = models.Employee.objects.get(id=data.get('assign_to'))
        except:
            assign_employee = None
        try:
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
        except:
            return Response(data={"error": "User doesn't have enough points."}, status=status.HTTP_400_BAD_REQUEST)
        profit_month = data.get('profit_month', 0)
        code_key = data.get('code_key', 0)
        username = data.get('username', '')
        password = data.get('password', '')
        if models.Client.objects.filter(email=data['email']):
            data = 'existed_email'
            return Response({'success': False, 'data': data})
        new_client = models.Client.objects.create(username=username, password=make_password(password),
                                                  email=email, location=data.get('location', ''),
                                                  first_name=first_name, last_name=last_name,
                                                  house_phone=data.get('house_phone', ''),
                                                  cell_phone=data.get('cell_phone', ''),
                                                  postal_address=data.get('postal_address', ''),
                                                  city=data.get('city',''), pays=data.get('pays', ''),
                                                  assign_to=assign_employee, code_key=code_key,
                                                  profit_month=profit_month, payment=data.get('payment', ''),
                                                  customer_type=data.get('customer_type', ''),
                                                  frequency=data.get('frequency', ''),
                                                  login_email=data.get('login_email', ''),
                                                  estimated_time=data.get('estimated_time',''),
                                                  replacement=data.get('replacement', ''), days=data.get('days', ''),
                                                  animals=data.get('animals',''), remarks=data.get('remarks', ''),
                                                  )
        new_client.save()
        cur_client = models.Client.objects.get(email=data['email'])
        original = self.serializer_class(cur_client)
        return Response({'success': True, 'data': original.data})

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
        if not models.Employee.objects.filter(id=request.data.get('assign_to')):
            mutable = request.POST._mutable
            request.POST._mutable = True
            request.data['assign_to'] = 5
            request.POST._mutable = mutable

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        original = Response(serializer.data).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

class EmployeeListView(APIView):
    serializer_class = serializers.EmployeeSerializer

    def get(self, request):
        employees = models.Employee.objects.filter(is_admin=False)
        serializer = self.serializer_class(employees, context={'request': request}, many=True)
        return Response({'success': True, 'data': serializer.data})

class EmployeeCreateView(APIView):
    serializer_class = serializers.ClientSerializer

    def post(self, request):
        data = request.data
        if models.Employee.objects.filter(email=data.get('email')):
            data = 'existed_email'
            return Response({'success': False, 'data': data})
        position = data.get('position', '')
        new_employee = models.Employee.objects.create(username=data.get('username'),
                                                      password=make_password(data.get('password')),
                                                      email=data.get('email'), position=position,
                                                      Supervisor=data.get('Supervisor'), note=data.get('note'))
        new_employee.save()
        cur_employee = models.Employee.objects.get(email=data.get('email'))
        original = self.serializer_class(cur_employee)
        return Response({'success': True, 'data': original.data})

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)


class ProspectListView(ListAPIView):
    serializer_class = serializers.ProspectSerializer
    pagination_class = SmallPagination

    def get(self, request, *args, **kwargs):
        clients = models.Prospect.objects.all()
        serializer = self.serializer_class(clients, context={'request': request}, many=True)
        page = self.paginate_queryset(serializer.data)
        serializer = self.get_paginated_response(page)
        return Response({'success': True, 'data': serializer.data})


class ProspectCreateView(APIView):
    serializer_class = serializers.ProspectSerializer

    def post(self, request):
        data = request.data
        try:
            assign_employee = models.Employee.objects.get(id=data.get('assign_to'))
        except:
            assign_employee = None
        try:
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
        except:
            return Response(data={"error": "User doesn't have enough points."}, status=status.HTTP_400_BAD_REQUEST)
        profit_month = data.get('profit_month', 0)
        code_key = data.get('code_key', 0)
        username = data.get('username', '')
        password = data.get('password', '')
        if models.Prospect.objects.filter(email=data.get('email')):
            data = 'existed_email'
            return Response({'success': False, 'data': data})
        new_prospect = models.Prospect.objects.create(username=username, password=make_password(password),
                                                      email=email, location=data.get('location', ''),
                                                      first_name=first_name, last_name=last_name,
                                                      house_phone=data.get('house_phone', ''),
                                                      cell_phone=data.get('cell_phone', ''),
                                                      postal_address=data.get('postal_address', ''),
                                                      city=data.get('city', ''), pays=data.get('pays', ''),
                                                      assign_to=assign_employee, code_key=code_key,
                                                      profit_month=profit_month, payment=data.get('payment', ''),
                                                      frequency=data.get('frequency', ''),
                                                      login_email=data.get('login_email', ''),
                                                      estimated_time=data.get('estimated_time', ''),
                                                      replacement=data.get('replacement', ''),
                                                      days=data.get('days', ''),
                                                      animals=data.get('animals', ''),
                                            )
        new_prospect.save()
        cur_prospect = models.Prospect.objects.get(email=email)
        original = self.serializer_class(cur_prospect)
        return Response({'success': True, 'data': original.data})

class ProspectEditAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Prospect.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.ProspectSerializer

    def get_queryset(self):
        return models.Prospect.objects.filter(id=self.request.id)

    def get_object(self):
        return get_object_or_404(models.Prospect, pk=self.kwargs['id'])

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
        if not models.Employee.objects.filter(id=request.data.get('assign_to')):
            mutable = request.POST._mutable
            request.POST._mutable = True
            request.data['assign_to'] = 5
            request.POST._mutable = mutable

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        original = Response(serializer.data).data
        my_data = {}
        for key, value in original.items():
            my_data[key] = value
        return Response({'success': True, 'data': my_data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', ])
def get_clientCount(request):
    count = models.Client.objects.filter(is_admin=False).count()
    return Response({'success': True, 'count': count})

@api_view(['GET', ])
def get_employeeCount(request):
    count = models.Employee.objects.filter(is_admin=False).count()
    return Response({'success': True, 'count': count})

@api_view(['GET', ])
def get_prospectCount(request):
    count = models.Prospect.objects.filter(is_admin=False).count()
    return Response({'success': True, 'count': count})