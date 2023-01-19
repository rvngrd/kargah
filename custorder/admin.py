from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
from .models import CustomerBuy, Product, BuyItem
# Register your models here.


class ItemInline(admin.TabularInline):
    model = BuyItem


@admin.register(CustomerBuy)
class Admin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ['id', 'employee', 'customer', 'datetime', 'description']
    list_filter = [
         ('datetime', JDateFieldListFilter),
    ]
    search_fields = (
        'id',
    )
