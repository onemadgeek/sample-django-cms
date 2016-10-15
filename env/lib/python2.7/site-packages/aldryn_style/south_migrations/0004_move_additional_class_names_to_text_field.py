# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for obj in orm.Style.objects.all():
            obj.txt_additional_class_names = obj.additional_class_names
            obj.save()

    def backwards(self, orm):
        for obj in orm.Style.objects.all():
            obj.additional_class_names = obj.txt_additional_class_names[0:200]
            obj.save()

    models = {
        u'aldryn_style.style': {
            'Meta': {'object_name': 'Style', '_ormbases': ['cms.CMSPlugin']},
            'additional_class_names': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'default': "'container'", 'max_length': '50', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'id_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'margin_bottom': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'margin_left': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'margin_right': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'margin_top': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'padding_bottom': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'padding_left': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'padding_right': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'padding_top': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'default': "'div'", 'max_length': '50'}),
            'txt_additional_class_names': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'cms.cmsplugin': {
            # NOTE: We've commented out a couple of fields below. This will
            # allow this data migration to actually work under 3.0 and 3.1
            # (where we switched to Treebeard). Manual testing shows that the
            # migration still works fine. Please do not un-comment these lines.
            # Further note that all of this will disappear once we stop
            # supporting Django 1.6.
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            # 'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            # 'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            # 'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            # 'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_style']
    symmetrical = True
