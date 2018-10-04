# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_auto_20160207_0534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name': 'sale', 'verbose_name_plural': 'sales'},
        ),
        migrations.AlterModelOptions(
            name='voucher',
            options={'verbose_name': 'voucher', 'verbose_name_plural': 'vouchers'},
        ),
        migrations.AlterField(
            model_name='sale',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.Product', verbose_name='products'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'USD'), ('percentage', '%')], default='fixed', max_length=10, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='apply_to',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='apply to'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='limit',
            field=django_prices.models.MoneyField(blank=True, currency='USD', decimal_places=2, max_digits=12, null=True, verbose_name='limit'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='product'),
        ),
    ]