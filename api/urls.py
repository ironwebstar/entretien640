from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    # path('auth/', include('rest_auth.urls')),
    # path('rest-auth/login/', ),s
    path('auth/login/', views.CustomLoginView.as_view(), name='auth_login'),
    path('auth/registration/', include('rest_auth.registration.urls')),

    # Client View
    path('clients/', views.ClientListView.as_view()),
    path('employees/', views.EmployeeListView.as_view()),
]