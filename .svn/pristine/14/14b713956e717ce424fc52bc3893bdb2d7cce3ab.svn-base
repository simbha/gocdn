# encoding: utf-8

from django.db import models
from django.contrib.admin.filterspecs import FilterSpec, ChoicesFilterSpec, RelatedFilterSpec
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _



class CategoryAdminFilter(FilterSpec):
    def __init__(self, f, request, params, model, model_admin, field_path=None):
        self.lookup_val = request.GET.get('parent', None)
        self.field = f

        self.lookup_choices = model.objects.filter(parent__id=self.lookup_val)

    def get_query_set(self, cl, qs):
        if self.lookup_val:
            qs = qs.filter(parent__id=self.lookup_val)
        
        return qs

    def choices(self, cl):
        yield {'selected': self.lookup_val is None,
               'query_string': cl.get_query_string({}, [self.field.name]),
               'display': _('All')}

        if len(self.lookup_choices) > 0:
            for choice in self.lookup_choices:
                yield {'selected': self.lookup_val == choice.id,
                        'query_string': cl.get_query_string({self.field.name: choice.id}),
                        'display': "%s %s" % (smart_unicode(choice), " (" + smart_unicode(choice.category_set.count()) + ")")
                }


'''
Urun provider_stock_code a gore filtreleme
bu alan dolu ise urun manuel eklenmemis xml den eklenmistir.
'''
class ProductAdminFilter(FilterSpec):
    def __init__(self, f, request, params, model, model_admin, field_path=None):
        self.lookup_val = request.GET.get('provider_stock_code__isnull', None)
        self.field = f

    def choices(self, cl):
        yield {'selected': self.lookup_val is None,
               'query_string': cl.get_query_string({}, [self.field.name]),
               'display': _('All')
               }
        
        yield {'selected': self.lookup_val == 'True',
               'query_string': cl.get_query_string({'provider_stock_code__isnull': True}, [self.field.name]),
               'display': _('Yes')
               }
        
        yield {'selected': self.lookup_val == 'False',
               'query_string': cl.get_query_string({'provider_stock_code__isnull': False}, [self.field.name]),
               'display': _('No')
               }

    def title(self):
        return "Manuel Eklenenler"



FilterSpec.filter_specs.insert(1, (lambda f: getattr(f, 'product_admin_filter', False), ProductAdminFilter))
FilterSpec.filter_specs.insert(0, (lambda f: bool(f.rel and hasattr(f, 'category_admin_filter')), CategoryAdminFilter))
#FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'category_admin_filter', False), CategoryAdminFilter))

