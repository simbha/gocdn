# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HelpSubject'
        db.create_table('helpdesk_helpsubject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('helpdesk', ['HelpSubject'])

        # Adding model 'Help'
        db.create_table('helpdesk_help', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('help_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('help_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['helpdesk.HelpSubject'])),
            ('help_content', self.gf('django.db.models.fields.TextField')()),
            ('help_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.GoUser'])),
        ))
        db.send_create_signal('helpdesk', ['Help'])


    def backwards(self, orm):
        # Deleting model 'HelpSubject'
        db.delete_table('helpdesk_helpsubject')

        # Deleting model 'Help'
        db.delete_table('helpdesk_help')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'helpdesk.help': {
            'Meta': {'object_name': 'Help'},
            'help_content': ('django.db.models.fields.TextField', [], {}),
            'help_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helpdesk.HelpSubject']"}),
            'help_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'help_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.GoUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'helpdesk.helpsubject': {
            'Meta': {'object_name': 'HelpSubject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'members.gouser': {
            'Meta': {'object_name': 'GoUser', '_ormbases': ['auth.User']},
            'activation_code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'address_1': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'fraud': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'tc_identity': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'user_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['helpdesk']