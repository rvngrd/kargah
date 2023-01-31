from django.db import models
from django_jalali.db import models as jmodels


class BuyRawMaterial(models.Model):
    class Meta:
        verbose_name = "ثبت خرید ماده اولیه"
        verbose_name_plural = "ثبت خرید ماده اولیه"
    objects = jmodels.jManager()
    employee = models.ForeignKey('accounts.Employee', on_delete=models.PROTECT, verbose_name='کارمند')
    datetime = jmodels.jDateTimeField('تاریخ')
    description = models.TextField('توضیحات', blank=True, null=True)

    def __str__(self):
        return 'شماره خرید ماده اولیه {}'.format(self.id)


class RawMaterial(models.Model):
    class Meta:
        verbose_name = "ماده اولیه"
        verbose_name_plural = "ماده اولیه"
    name = models.CharField('نام', max_length=30)
    man_factory = models.CharField('کارخانه سازنده', max_length=30)

    def __str__(self):
        return '{} - {}'.format(self.name, self.man_factory)


class BuyRawItem(models.Model):
    class Meta:
        verbose_name = "ردیف ماده اولیه"
        verbose_name_plural = "ردیف ماده اولیه"
    buy_rawmaterial = models.ForeignKey('BuyRawMaterial', on_delete=models.PROTECT, verbose_name='آیدی خرید ماده اولیه')
    raw_material = models.ForeignKey('RawMaterial', on_delete=models.PROTECT, verbose_name='ماده اولیه')
    quantity = models.IntegerField('تعداد')
    price = models.IntegerField('قیمت')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.buy_rawmaterial, self.raw_material, self.quantity, self.price)
