# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 11:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('part', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.PositiveIntegerField(blank=True, help_text='Serial number for this item', null=True)),
                ('URL', models.URLField(blank=True, max_length=125)),
                ('batch', models.CharField(blank=True, help_text='Batch code for this stock item', max_length=100)),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('updated', models.DateField(auto_now=True)),
                ('stocktake_date', models.DateField(blank=True, null=True)),
                ('review_needed', models.BooleanField(default=False)),
                ('status', models.PositiveIntegerField(choices=[(10, 'OK'), (60, 'Destroyed'), (50, 'Attention needed'), (55, 'Damaged')], default=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('notes', models.TextField(blank=True)),
                ('infinite', models.BooleanField(default=False)),
                ('belongs_to', models.ForeignKey(blank=True, help_text='Is this item installed in another item?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_parts', to='stock.StockItem')),
                ('customer', models.ForeignKey(blank=True, help_text='Item assigned to customer?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stockitems', to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='StockItemTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('notes', models.TextField(blank=True)),
                ('system', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_info', to='stock.StockItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='stock.StockLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stockitem',
            name='location',
            field=models.ForeignKey(blank=True, help_text='Where is this stock item located?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='stock.StockLocation'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='part.Part'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='stocktake_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='supplier_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.SupplierPart'),
        ),
        migrations.AlterUniqueTogether(
            name='stocklocation',
            unique_together=set([('name', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='stockitem',
            unique_together=set([('part', 'serial')]),
        ),
    ]
