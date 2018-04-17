# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0019_auto_20180416_1249'),
        ('customer_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, help_text='Date order entered in system'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorder',
            name='customer_ref',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='internal_ref',
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorder',
            name='issued_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='Date order issued by customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorder',
            name='notes',
            field=models.TextField(blank=True, default='', help_text='Order notes'),
        ),
        migrations.AddField(
            model_name='customerorderline',
            name='notes',
            field=models.TextField(blank=True, help_text='Line notes'),
        ),
        migrations.AddField(
            model_name='customerorderline',
            name='part',
            field=models.ForeignKey(default=0, help_text='Part', on_delete=django.db.models.deletion.CASCADE, to='part.Part'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorderline',
            name='quantity',
            field=models.IntegerField(default=1, help_text='Quantity of part'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerorderline',
            name='customer_order',
            field=models.ForeignKey(help_text='Order this line belongs to', on_delete=django.db.models.deletion.CASCADE, to='customer_orders.CustomerOrder'),
        ),
        migrations.AlterField(
            model_name='customerorderline',
            name='line_number',
            field=models.PositiveIntegerField(default=0, help_text='Line number'),
        ),
    ]
