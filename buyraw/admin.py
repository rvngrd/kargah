from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
from .models import BuyRawMaterial, RawMaterial, BuyRawItem
# Register your models here.

import django_jalali.admin as jadmin


class ItemInline(admin.TabularInline):
    model = BuyRawItem


@admin.register(BuyRawMaterial)
class BuyRawMatdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    exclude = ['employee', ]
    list_display = ['id', 'employee', 'datetime', 'description']
    list_filter = [
         ('datetime', JDateFieldListFilter),
         'employee'
    ]
    search_fields = (
        'id',
    )

    def save_model(self, request, obj, form, change):
        # associating the current logged-in user to the employee
        obj.employee = request.user.employee
        super().save_model(request, obj, form, change)


@admin.register(RawMaterial)
class RawMatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'man_factory']
    list_filter = ['man_factory', ]
    search_fields = (
        'id',
    )
