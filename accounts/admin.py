from django.contrib import admin
from .models import Employee, Customer


# Register your models here.


@admin.register(Employee)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lname', 'rank', 'ncode')
    list_filter = [
         'rank'
    ]
    search_fields = (
        'id', 'ncode'
    )


@admin.register(Customer)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lname', 'ncode', 'email', 'address')
