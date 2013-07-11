# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MainPage.abstract'
        db.add_column('home_mainpage', 'abstract',
                      self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MainPage.add_date'
        db.add_column('home_mainpage', 'add_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MainPage.abstract'
        db.delete_column('home_mainpage', 'abstract')

        # Deleting field 'MainPage.add_date'
        db.delete_column('home_mainpage', 'add_date')


    models = {
        'home.mainpage': {
            'Meta': {'object_name': 'MainPage'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['home.Positions']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'home.positions': {
            'Meta': {'object_name': 'Positions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']