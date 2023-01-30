from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    """
    Represents employees
    """
    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    # fields that are stored in User: user_name, password, email, date_joined

    ncode = models.CharField('کدملی', max_length=11)
    name = models.CharField('نام', max_length=20)
    lname = models.CharField('نام خانوادگی', max_length=20)
    MANAGER = 1
    NOT_MANAGER = 2
    RANK_CHOICES = (
        (MANAGER, 'مدیر فروش'),
        (NOT_MANAGER, 'کارمند فروش')
    )
    rank = models.IntegerField('سمت', choices=RANK_CHOICES)

    def __str__(self):
        return self.user.get_full_name()


class Customer(models.Model):
    """
    Represents customers
    """
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

    ncode = models.CharField('کدملی', max_length=11)
    name = models.CharField('نام', max_length=20)
    lname = models.CharField('نام خانوادگی', max_length=20)
    email = models.EmailField('ایمیل', null=True, blank=True)
    address = models.TextField('آدرس', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.lname)


class EmployeePhone(models.Model):
    """
    Represents Employees phone number
    """
    class Meta:
        verbose_name = 'شماره تماس کارمند'
        verbose_name_plural = 'شماره تماس کارمند'

    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name='کارمند')
    phone = models.CharField('شماره تماس', max_length=11)

    def __str__(self):
        return '{} - {}'.format(self.employee, self.phone)


class CustomerPhone(models.Model):
    """
    Represents Customers phone number
    """

    class Meta:
        verbose_name = 'شماره تماس مشتری'
        verbose_name_plural = 'شماره تماس مشتری'

    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, verbose_name='کارمند')
    phone = models.CharField('شماره تماس', max_length=11)

    def __str__(self):
        return '{} - {}'.format(self.customer, self.phone)
