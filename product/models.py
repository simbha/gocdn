# encoding: utf-8
from django.db import models
from django.utils import encoding

EXCHANGES = ((0, "TL"),
             (1, "USD"),
             (2, "EUR"))
class ProductCategory(models.Model):
    name = models.CharField(verbose_name=u'Kategori ismi',max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(verbose_name=u'Açıklama')
    is_active = models.BooleanField(default=True,verbose_name=u'Aktif mi')
    meta_keywords = models.CharField('Meta kelimeleri',max_length=255)
    meta_description = models.CharField("Meta Açıklamaları", max_length=255)
    created_at = models.DateTimeField(verbose_name=u'Oluşturma Zamanı',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=u'Güncelleme Zamanı',auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name = u'Kategori'
        verbose_name_plural = u'kategoriler'
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True,verbose_name=u'İsim')
    slug = models.SlugField(max_length=255, unique=True, help_text='isimle aynı olmalıdır')
    brand = models.CharField(max_length=50,verbose_name=u'Marka')
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2,verbose_name=u'Fiyat')
    old_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00,verbose_name=u'Eski Fiyat')
    exchange_type = models.SmallIntegerField("Para Birimi", choices=EXCHANGES, default=0)
    image = models.CharField(max_length=50,verbose_name=u'Resim')
    is_active = models.BooleanField(default=True,verbose_name=u'Aktif mi?')
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(verbose_name=u'Miktar')
    description = models.TextField(verbose_name=u'Açıklama')
    meta_keywords = models.CharField(max_length=255, help_text='Comma ile ayırınız')
    meta_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=u'Oluşturma Zamanı')
    updated_at = models.DateTimeField(auto_now=True,verbose_name=u'Güncelleme zamanı')
    categories = models.ManyToManyField(ProductCategory,verbose_name=u'kategori')

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = u'Product'
        verbose_name_plural = u'Product'

    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None

class Country(models.Model):
    country = models.CharField(max_length=255,verbose_name=u'Ülke')
    country_order = models.IntegerField(verbose_name=u'Sıra')

    def __unicode__(self):
        return self.country


    class Meta:
        verbose_name = u'Country'
        verbose_name_plural = u'Country'


class Pricing(models.Model):
    pricing_country = models.ForeignKey(Country, verbose_name=u'Ülke',related_name='pricing_country', default=1)
    exchange_type = models.SmallIntegerField("Para Birimi", choices=EXCHANGES, default=0)
    price_per_gb = models.DecimalField(max_digits=9,decimal_places=3,verbose_name=u'Gigabyte Fiyatı')
    price_per_tb = models.DecimalField(max_digits=9,decimal_places=3,verbose_name=u'Terabyte Fiyatı')


    class Meta:
        verbose_name = u'Fiyat'
        verbose_name_plural = u'Fiyat'

    def get_gb_price(self):
        return self.price_per_gb

    def get_tb_price(self):
        return self.price_per_gb * 1000
