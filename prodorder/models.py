from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.


class ProductionOrder(models.Model):
    """
    Represents production order model
    """

    class Meta:
        verbose_name = 'ثبت تولید'
        verbose_name_plural = 'ثبت تولید'
    objects = jmodels.jManager()
    employee = models.ForeignKey('accounts.Employee', on_delete=models.PROTECT, verbose_name='کارمند')
    product = models.ForeignKey('custorder.Product', on_delete=models.PROTECT, verbose_name='محصول')
    quantity = models.IntegerField('تعداد')
    datetime = jmodels.jDateTimeField('تاریخ', auto_now_add=True)
    description = models.TextField('توضیحات', blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.employee, self.product, self.quantity)
