from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # Client View
    path('clients/', views.ClientListView.as_view()),
    path('employees/', views.EmployeeListView.as_view()),
]