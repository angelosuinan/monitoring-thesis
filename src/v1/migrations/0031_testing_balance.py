# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-14 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0030_testing_contract_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='balance',
            field=models.CharField(default='wit', max_length=100),
            preserve_default=False,
        ),
    ]
