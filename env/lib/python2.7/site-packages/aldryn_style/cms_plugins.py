# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from aldryn_style.models import Style


class StylePlugin(CMSPluginBase):
    model = Style
    name = _("Style")
    render_template = "aldryn_style/plugin.html"
    allow_children = True

    fieldsets = (
        (None, {
            'fields': ('label', 'class_name', )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'additional_class_names',
                'id_name',
                ('padding_top', 'padding_right', 'padding_bottom',
                 'padding_left'),
                ('margin_top', 'margin_right', 'margin_bottom', 'margin_left'),
            ),
        }),
    )

plugin_pool.register_plugin(StylePlugin)
