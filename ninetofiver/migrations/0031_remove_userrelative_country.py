# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninetofiver', '0030_auto_20170220_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrelative',
            name='country',
        ),
    ]
