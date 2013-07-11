# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customers'
        db.create_table('home_customers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('home', ['Customers'])


    def backwards(self, orm):
        # Deleting model 'Customers'
        db.delete_table('home_customers')


    models = {
        'home.customers': {
            'Meta': {'object_name': 'Customers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'home.mainpage': {
            'Meta': {'object_name': 'MainPage'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'footer_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_slogan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'middle_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['home.Positions']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'top_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'home.positions': {
            'Meta': {'object_name': 'Positions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']