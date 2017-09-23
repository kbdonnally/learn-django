# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170922_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, null=True), # 'unique=True' -> 'null=True'
        ),
    ]
