# Generated by Django 4.1.5 on 2023-01-15 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncode', models.CharField(max_length=11, verbose_name='کدملی')),
                ('name', models.CharField(max_length=20, verbose_name='نام')),
                ('lname', models.CharField(max_length=20, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncode', models.CharField(max_length=11, verbose_name='کدملی')),
                ('name', models.CharField(max_length=20, verbose_name='نام')),
                ('lname', models.CharField(max_length=20, verbose_name='نام خانوادگی')),
                ('rank', models.IntegerField(choices=[(1, 'مدیر فروش'), (2, 'کارمند فروش')], verbose_name='سمت')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نمایه کارمند')),
            ],
            options={
                'verbose_name': 'نمایه کارمند',
                'verbose_name_plural': 'نمایه کارمندان',
            },
        ),
    ]
