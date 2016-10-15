# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_style', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='class_name',
            field=models.CharField(default=b'container', max_length=50, verbose_name='class name', blank=True, choices=[(b'container', 'bootstrap container')]),
            preserve_default=True,
        ),
    ]
