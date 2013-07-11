# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductCategory'
        db.create_table('categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('product', ['ProductCategory'])

        # Adding model 'Product'
        db.create_table('products', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('old_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2, blank=True)),
            ('exchange_type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_bestseller', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('product', ['Product'])

        # Adding M2M table for field categories on 'Product'
        db.create_table('products_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['product.product'], null=False)),
            ('productcategory', models.ForeignKey(orm['product.productcategory'], null=False))
        ))
        db.create_unique('products_categories', ['product_id', 'productcategory_id'])

        # Adding model 'Country'
        db.create_table('product_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('product', ['Country'])

        # Adding model 'Pricing'
        db.create_table('product_pricing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pricing_country', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='pricing_country', to=orm['product.Country'])),
            ('exchange_type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('price_per_gb', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=3)),
            ('price_per_tb', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=3)),
        ))
        db.send_create_signal('product', ['Pricing'])


    def backwards(self, orm):
        # Deleting model 'ProductCategory'
        db.delete_table('categories')

        # Deleting model 'Product'
        db.delete_table('products')

        # Removing M2M table for field categories on 'Product'
        db.delete_table('products_categories')

        # Deleting model 'Country'
        db.delete_table('product_country')

        # Deleting model 'Pricing'
        db.delete_table('product_pricing')


    models = {
        'product.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country_order': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'product.pricing': {
            'Meta': {'object_name': 'Pricing'},
            'exchange_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_per_gb': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'price_per_tb': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '3'}),
            'pricing_country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'pricing_country'", 'to': "orm['product.Country']"})
        },
        'product.product': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Product', 'db_table': "'products'"},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['product.ProductCategory']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'exchange_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_bestseller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'old_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'product.productcategory': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'ProductCategory', 'db_table': "'categories'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['product']