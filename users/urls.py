from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.CustomUserListView.as_view()),
]