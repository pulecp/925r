# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 19:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=255, unique=True)),
                ('internal', models.BooleanField(default=False)),
                ('vat_identification_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid VAT identification number', regex='^[A-Z]{2}[a-zA-Z0-9]{2,13}$')])),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.company_set+', to='contenttypes.ContentType')),
                ('address', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'companies',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('legal_country', django_countries.fields.CountryField(max_length=2)),
                ('started_at', models.DateField()),
                ('ended_at', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.Company')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.employmentcontract_set+', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=255, unique=True)),
                ('monday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('tuesday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('wednesday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('thursday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('friday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('saturday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('sunday', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ninetofiver.workschedule_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='employmentcontract',
            name='work_schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ninetofiver.WorkSchedule'),
            preserve_default=False,
        ),
    ]
