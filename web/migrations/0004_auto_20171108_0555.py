# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20171107_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citymapping',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not Verified'), (1, 'User Verified'), (2, 'System Verified'), (3, 'Rejected')], default=0),
        preserve_default=True,
        ),
    ]