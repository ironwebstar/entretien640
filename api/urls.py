from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    # path('auth/', include('rest_auth.urls')),
    # path('rest-auth/login/', ),s
    path('auth/login/', views.CustomLoginView.as_view(), name='auth_login'),
    path('auth/registration/', include('rest_auth.registration.urls')),

    # Client View
    path('clients/', views.ClientListView.as_view(), name='clients_list'),
    path('clients/create', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:id>/', views.ClientEditAPIView.as_view(), name='client_edit'),

    path('count/client/', views.get_clientCount, name='client_count'),

    # Employee View
    path('employees/', views.EmployeeListView.as_view()),
    path('employees/create', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:id>/', views.EmployeeEditAPIView.as_view(), name='employee_edit'),

    path('count/employee/', views.get_employeeCount, name='employee_count'),

    # Prospect View
    path('prospects/', views.ProspectListView.as_view()),
    path('prospects/create', views.ProspectCreateView.as_view(), name='prospect_create'),
    path('prospects/<int:id>/', views.ProspectEditAPIView.as_view(), name='prospect_edit'),

    path('count/prospect/', views.get_prospectCount, name='prospect_count'),
]
