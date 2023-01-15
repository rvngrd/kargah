from django.contrib import admin
from .models import Employee, Customer


# Register your models here.


@admin.register(Employee)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('ncode', 'name', 'lname', 'rank')


@admin.register(Customer)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('ncode', 'name', 'lname', 'email', 'address')
