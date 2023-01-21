from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
from .models import CustomerBuy, Product, BuyItem
# Register your models here.

import django_jalali.admin as jadmin


class ItemInline(admin.TabularInline):
    model = BuyItem


@admin.register(CustomerBuy)
class Admin(admin.ModelAdmin):
    inlines = [ItemInline]
    exclude = ['employee', ]
    list_display = ['id', 'employee', 'customer', 'datetime', 'description']
    list_filter = [
         ('datetime', JDateFieldListFilter),
    ]
    search_fields = (
        'id',
    )

    def save_model(self, request, obj, form, change):
        # associating the current logged-in user to the employee
        obj.employee = request.user.employee
        super().save_model(request, obj, form, change)
