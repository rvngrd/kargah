# Generated by Django 4.1.5 on 2023-01-30 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_employeephone_customerphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerphone',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.customer', verbose_name='کارمند'),
        ),
    ]