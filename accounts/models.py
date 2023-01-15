from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    """
    Represents employees
    """
    class Meta:
        verbose_name = "نمایه کارمند"
        verbose_name_plural = "نمایه کارمند"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نمایه کارمند')
    # fields that are stored in User: first_name, last_name, email, date_joined

    ncode = models.CharField('کدملی', max_length=11)
    MANAGER = 1
    NOT_MANAGER = 2
    RANK_CHOICES = {
        'MANAGER': 'مدیر فروش',
        'NOT_MANAGER': 'کارمند فروش'
    }
    rank = models.IntegerField('سمت', choices=RANK_CHOICES)
