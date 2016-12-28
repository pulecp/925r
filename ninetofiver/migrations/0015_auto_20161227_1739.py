# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 17:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0014_consultancycontract_projectcontract_supportcontract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperformance',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(24)]),
        ),
    ]