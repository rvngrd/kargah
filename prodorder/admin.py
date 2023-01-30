from django.contrib import admin

# Register your models here.
from django_jalali.admin.filters import JDateFieldListFilter
from prodorder.models import ProductionOrder


@admin.register(ProductionOrder)
class CustBuyAdmin(admin.ModelAdmin):
    exclude = ['employee', ]
    list_display = ['id', 'employee', 'product', 'quantity', 'datetime', 'description']
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
