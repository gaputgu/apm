import django_tables2 as tables
from django_tables2.utils import A
from .models import shipClass, shipInstance, maintenanceItem, supplyPart

class shipClassTable(tables.Table):
    """Table for shipClass model"""
    name = tables.LinkColumn('ship_class_view',args=[A('name')])
    class Meta:
        model = shipClass
        fields = ('name',)
        attrs  = {'class': 'generic'}
        row_attr = {
            'data-id': lambda record:record.pk
        }

class shipInstanceTable(tables.Table):
    """Table for shipInstance model"""
    name = tables.LinkColumn('ship_instance_view',args=[A('name')])
    class Meta:
        model = shipInstance
        fields = ('name','identifier','availability')
        attrs  = {'class': 'generic'}
        row_attr = {
            'data-id': lambda record:record.pk
        }

class maintenanceItemTable(tables.Table):
    title = tables.LinkColumn('maintenance_item_view',args=[A('title')])
    class Meta:
        model = maintenanceItem
        fields = ('title','description','cfid','periodicity','driver')
        attrs  = {'class': 'generic'}
        row_attr = {
            'data-id': lambda record:record.pk
        }

class supplyPartTable(tables.Table):
    class Meta:
        model = supplyPart
        fields = ('NIIN', 'PN', 'FSC','itemDescription')
        attrs  = {'class': 'generic'}
        row_attr = {
            'data-id': lambda record:record.pk
        }
