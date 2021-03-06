# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0025_auto_20170911_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualCommandLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('command', models.CharField(max_length=10)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Subscriber')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
