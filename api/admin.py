from django.contrib import admin
from django import forms
# Register your models here.
from .models import Employee, Client

class EmployeeAdmin(admin.ModelAdmin):
    # form = EmployeeForm
    list_display = ('username', 'email', 'position', 'Supervisor', 'note', 'pays' )

admin.site.register(Employee, EmployeeAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'customer_type', 'frequency', 'assign_to', 'cell_phone', 'profit_month')

admin.site.register(Client, ClientAdmin)
