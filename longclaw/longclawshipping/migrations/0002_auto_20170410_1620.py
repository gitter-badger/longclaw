# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 16:20
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('longclawshipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]