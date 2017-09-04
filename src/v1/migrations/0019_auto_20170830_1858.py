# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0018_report_latest_sampling_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='fish_weight',
            new_name='average_fishes_weight',
        ),
        migrations.RemoveField(
            model_name='report',
            name='fish_length',
        ),
        migrations.RemoveField(
            model_name='report',
            name='fish_width',
        ),
        migrations.RemoveField(
            model_name='report',
            name='latest_sampling_result',
        ),
    ]