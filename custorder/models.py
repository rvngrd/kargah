from django.db import models

from django_jalali.db import models as jmodels
# Create your models here.


class CustomerBuy(models.Model):
    objects = jmodels.jManager()
    employee = models.ForeignKey('accounts.Employee', on_delete=models.PROTECT, verbose_name='کارمند')
    customer = models.ForeignKey('accounts.Customer', on_delete=models.PROTECT, verbose_name='مشتری')
    datetime = jmodels.jDateTimeField('تاریخ')
    description = models.TextField('توضیحات', blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.employee, self.customer, self.datetime)


class Product(models.Model):
    objects = jmodels.jManager()
    ROGHAN = 1
    ZAFERAN = 2
    TYPE_CHOICE = (
        (ROGHAN, 'روغن حیوانی'),
        (ZAFERAN, 'زعفران')
    )
    type = models.IntegerField('نوع', choices=TYPE_CHOICE)
    weight = models.IntegerField('وزن(گرم)')
    product_serie = models.IntegerField('سری ساخت')
    man_date = jmodels.jDateField('تاریخ تولید')
    exp_date = jmodels.jDateField('تاریخ انقضا')

    def __str__(self):
        return '{} - {} - {}'.format(self.type, self.weight, self.product_serie)


class BuyItem(models.Model):
    customerbuy = models.ForeignKey('CustomerBuy', on_delete=models.PROTECT, verbose_name='آیدی خرید')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='محصول')
    quantity = models.IntegerField('تعداد')
    price = models.IntegerField('قیمت')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.customerbuy, self.product, self.quantity, self.price)
