# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainPage'
        db.create_table('home_mainpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['MainPage'])


    def backwards(self, orm):
        # Deleting model 'MainPage'
        db.delete_table('home_mainpage')


    models = {
        'home.mainpage': {
            'Meta': {'object_name': 'MainPage'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['home']