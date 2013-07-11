# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faqs'
        db.create_table('faq_faqs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('faq', ['Faqs'])


    def backwards(self, orm):
        # Deleting model 'Faqs'
        db.delete_table('faq_faqs')


    models = {
        'faq.faqs': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Faqs'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['faq']