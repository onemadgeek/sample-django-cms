# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

import warnings

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


CLASS_NAMES = getattr(
    settings,
    'ALDRYN_STYLE_CLASS_NAMES',
    (
        ('container', _('container')),
        ('content', _('content')),
        ('teaser', _('teaser')),
    )
)

CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')
TAG_TYPE_FORMAT = re.compile(r'\w[\w\d]*$')


def get_html_tag_types():
    tag_types = getattr(settings, 'ALDRYN_STYLE_ALLOWED_TAGS', None)
    if tag_types:
        # Remove anything that doesn't look like an HTML tag
        for tag in tag_types:
            tag = tag.strip()
            if not TAG_TYPE_FORMAT.match(tag):
                warnings.warn(_('ALDRYN STYLE: "{0}" was omitted from '
                                'ALDRYN_STYLE_ALLOWED_TAGS as it does '
                                'not look like a valid HTML tag.').format(tag))
                tag_types.remove(tag)

    # Could be that it was initially empty, or, none of the supplied entries
    # looked right, in either of these cases, use the default set as defined
    # in version 1.0.1.
    if not tag_types:
        tag_types = [
            'div', 'article', 'section', 'span', 'p', 'h1', 'h2', 'h3', 'h4',
        ]

    return tuple([(tag, tag) for tag in tag_types])


@python_2_unicode_compatible
class Style(CMSPlugin):
    """
    A CSS Style Plugin
    """
    DIV_TAG = 'div'
    HTML_TAG_TYPES = get_html_tag_types()

    label = models.CharField(
        _('label'), max_length=128, default='', blank=True,
        help_text=_('Optional label for this style plugin.'))
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin, related_name='+', parent_link=True)
    class_name = models.CharField(
        _('class name'), choices=CLASS_NAMES, default=CLASS_NAMES[0][0],
        max_length=50, blank=True)
    id_name = models.CharField(
        _('id name'), max_length=50, blank=True, default='')
    tag_type = models.CharField(
        verbose_name=_('tag Type'), max_length=50, choices=HTML_TAG_TYPES,
        default=DIV_TAG)

    padding_top = models.SmallIntegerField(
        _('padding top'), blank=True, null=True)
    padding_right = models.SmallIntegerField(
        _('padding right'), blank=True, null=True)
    padding_bottom = models.SmallIntegerField(
        _('padding bottom'), blank=True, null=True)
    padding_left = models.SmallIntegerField(
        _('padding left'), blank=True, null=True)

    margin_top = models.SmallIntegerField(
        _('margin top'), blank=True, null=True)
    margin_right = models.SmallIntegerField(
        _('margin right'), blank=True, null=True)
    margin_bottom = models.SmallIntegerField(
        _('margin bottom'), blank=True, null=True)
    margin_left = models.SmallIntegerField(
        _('margin left'), blank=True, null=True)

    additional_class_names = models.TextField(
        verbose_name=_('additional classes'),
        blank=True,
        help_text=_('Comma separated list of additional classes to apply to '
                    'tag_type')
    )

    def __str__(self):
        display = self.tag_type or ''
        if self.additional_class_names:
            display = '{0} ({1})'.format(display, self.additional_class_names)
        if self.label:
            display = '“{0}”: {1}'.format(self.label, display)
        return display

    def clean(self):
        if self.additional_class_names:
            additional_class_names = list(
                html_class.strip() for html_class in
                self.additional_class_names.split(','))
            for class_name in additional_class_names:
                class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(class_name):
                    raise ValidationError(
                        _('"{0}" is not a proper css class name.').format(
                            class_name)
                    )
            self.additional_class_names = ', '.join(
                set(additional_class_names))

    @property
    def get_additional_class_names(self):
        if self.additional_class_names:
            # Removes any extra spaces
            return ' '.join((
                html_class.strip() for html_class in
                self.additional_class_names.split(',')))
        return ''

    @property
    def inline_style(self):
        styles = []
        if self.padding_top:
            styles.append('padding-top: {0:d}px;'.format(self.padding_top))
        if self.padding_right:
            styles.append('padding-right: {0:d}px;'.format(self.padding_right))
        if self.padding_bottom:
            styles.append('padding-bottom: {0:d}px;'.format(self.padding_bottom))
        if self.padding_left:
            styles.append('padding-left: {0:d}px;'.format(self.padding_left))
        if self.margin_top:
            styles.append('margin-top: {0:d}px;'.format(self.margin_top))
        if self.margin_right:
            styles.append('margin-right: {0:d}px;'.format(self.margin_right))
        if self.margin_bottom:
            styles.append('margin-bottom: {0:d}px;'.format(self.margin_bottom))
        if self.margin_left:
            styles.append('margin-left: {0:d}px;'.format(self.margin_left))
        return ' '.join(styles)
