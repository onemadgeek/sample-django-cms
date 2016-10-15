# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('label', models.CharField(default=b'', help_text='Optional label for this style plugin.', max_length=128, verbose_name='label', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('class_name', models.CharField(default=b'info', max_length=50, verbose_name='class name', blank=True, choices=[(b'info', b'info'), (b'new', b'new'), (b'hint', b'hint')])),
                ('id_name', models.CharField(default=b'', max_length=50, verbose_name='id name', blank=True)),
                ('tag_type', models.CharField(default=b'div', max_length=50, verbose_name='tag Type', choices=[(b'div', 'div'), (b'article', 'article'), (b'section', 'section'), (b'span', 'inline')])),
                ('padding_left', models.SmallIntegerField(null=True, verbose_name='padding left', blank=True)),
                ('padding_right', models.SmallIntegerField(null=True, verbose_name='padding right', blank=True)),
                ('padding_top', models.SmallIntegerField(null=True, verbose_name='padding top', blank=True)),
                ('padding_bottom', models.SmallIntegerField(null=True, verbose_name='padding bottom', blank=True)),
                ('margin_left', models.SmallIntegerField(null=True, verbose_name='margin left', blank=True)),
                ('margin_right', models.SmallIntegerField(null=True, verbose_name='margin right', blank=True)),
                ('margin_top', models.SmallIntegerField(null=True, verbose_name='margin top', blank=True)),
                ('margin_bottom', models.SmallIntegerField(null=True, verbose_name='margin bottom', blank=True)),
                ('additional_class_names', models.TextField(help_text='Comma separated list of additional classes to apply to tag_type', verbose_name='additional classes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
