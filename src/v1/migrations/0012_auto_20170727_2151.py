# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0011_auto_20170727_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='context',
            field=models.TextField(max_length=300),
        ),
    ]
