from django.contrib import admin
from .models import Employee, Customer, CustomerPhone, EmployeePhone


# Register your models here.

class EPhoneInline(admin.TabularInline):
    model = EmployeePhone


class CPhoneInline(admin.TabularInline):
    model = CustomerPhone


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EPhoneInline]
    list_display = ['id', 'name', 'lname', 'rank', 'ncode', 'user']
    list_filter = [
         'rank'
    ]
    search_fields = (
        'id', 'ncode'
    )

    # def username(self, obj):
    #     return obj.user.username

# obj.user.first_name + ' ' + obj.user.last_name


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CPhoneInline]
    list_display = ('id', 'name', 'lname', 'ncode', 'email', 'address')
    search_fields = (
        'id', 'ncode'
    )
