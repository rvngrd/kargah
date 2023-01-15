from django.contrib import admin
from .models import Employee, Customer


# Register your models here.


@admin.register(Employee)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['user.get_full_name()', 'ncode', 'rank']


@admin.register(Customer)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['ncode', 'name', 'lname', 'email', 'address']
