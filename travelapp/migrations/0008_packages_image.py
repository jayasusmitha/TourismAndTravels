# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0007_auto_20170704_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='image',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]