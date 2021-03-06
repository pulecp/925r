# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ninetofiver', '0003_auto_20161220_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.holiday_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
