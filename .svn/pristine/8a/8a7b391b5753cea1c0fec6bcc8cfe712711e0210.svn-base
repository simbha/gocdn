# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Cdn.url_signing'
        db.alter_column('cdn_cdn', 'url_signing_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['cdn.UrlSigning']))

        # Changing field 'Cdn.static_url'
        db.alter_column('cdn_cdn', 'static_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Cdn.url_signing'
        db.alter_column('cdn_cdn', 'url_signing_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cdn.UrlSigning']))

        # User chose to not deal with backwards NULL issues for 'Cdn.static_url'
        raise RuntimeError("Cannot reverse this migration. 'Cdn.static_url' and its values cannot be restored.")

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
        'cdn.cacheexpiry': {
            'Meta': {'object_name': 'CacheExpiry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cdn.cdn': {
            'Meta': {'object_name': 'Cdn'},
            'cache_expiry': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'cdn_cache'", 'null': 'True', 'blank': 'True', 'to': "orm['cdn.CacheExpiry']"}),
            'cdn': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cdn_types': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cdn_types'", 'to': "orm['cdn.CdnTypes']"}),
            'cdn_urls': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cdn_users': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cdn_user'", 'to': "orm['members.GoUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'original_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'push_zone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cdn_push'", 'to': "orm['cdn.PushZones']"}),
            'static_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url_signing': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'cdn_signing'", 'null': 'True', 'blank': 'True', 'to': "orm['cdn.UrlSigning']"})
        },
        'cdn.cdntypes': {
            'Meta': {'object_name': 'CdnTypes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cdn.pushservers': {
            'Meta': {'object_name': 'PushServers'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cdn.pushzones': {
            'Meta': {'object_name': 'PushZones'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'push_server'", 'null': 'True', 'blank': 'True', 'to': "orm['cdn.PushServers']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'push_user'", 'null': 'True', 'blank': 'True', 'to': "orm['members.GoUser']"})
        },
        'cdn.urlsigning': {
            'Meta': {'object_name': 'UrlSigning'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['cdn']