# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0016_auto_20170830_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='feed_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='fish_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='fish_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='fish_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]