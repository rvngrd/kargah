from django.contrib import admin
from .models import Employee, Customer


# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lname', 'rank', 'ncode', 'emp_name')
    list_filter = [
         'rank'
    ]
    search_fields = (
        'id', 'ncode'
    )

    def emp_name(self, obj):
        return obj.user.first_name + obj.user.last_name


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lname', 'ncode', 'email', 'address')
    search_fields = (
        'id', 'ncode'
    )
