# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teapp', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_details',
            name='duration',
        ),
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='streams',
            name='stream',
            field=models.CharField(max_length=40),
        ),
    ]
