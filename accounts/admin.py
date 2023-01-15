from django.contrib import admin
from .models import Employee

# Register your models here.


@admin.register(Employee)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['user.get_full_name()', 'ncode', 'rank']
