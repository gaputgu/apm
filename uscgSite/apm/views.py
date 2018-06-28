from django.shortcuts import render
from .models import productLine, shipClass, shipInstance,maintenanceItem
from .models import maintenanceRequirementList, supplyPart
from .tables import shipClassTable, shipInstanceTable,maintenanceItemTable
from .tables import supplyPartTable
# Create your views here.

def home(request):
    """View for Home Page"""
    product_lines = productLine.objects.all()
    return render(request,
        'home.html',
        context = {
            'product_lines': product_lines,
        })

def product_line_view(request,name):
    """View Function for Product Lines"""
    product_lines = productLine.objects.all()
    product_line_filter = productLine.objects.get(name=name)
    kwargs = {'productLine':product_line_filter}
    table = shipClassTable(shipClass.objects.filter(**kwargs))
    return render(request,
        'apm/product_line_view.html',
        context = {
        'product_lines': product_lines,
        'productLineFilter':product_line_filter,
        'table':table}
        )

def ship_class_view(request,name):
    """View Function for Ship Class"""
    product_lines = productLine.objects.all()
    ship_class_filter = shipClass.objects.get(name=name)
    kwargs = {'shipClass':ship_class_filter}
    table = shipInstanceTable(shipInstance.objects.filter(**kwargs))
    return render(request,
        'apm/ship_class_view.html',
        context = {
            'product_lines': product_lines,
            'ship_class': ship_class_filter,
            'table':table
        })

def ship_instance_view(request,name):
    """View Function for Ship Instance"""
    product_lines = productLine.objects.all()
    ship_instance_filter = shipInstance.objects.get(name=name)
    kwargs_si = {'shipInstance':ship_instance_filter}
    #Filter for maintenance requirement list
    mrl = maintenanceRequirementList.objects.get(**kwargs_si)
    kwargs_mrl = {'maintenanceRequirementList': mrl}
    mrl_filter = maintenanceItem.objects.filter(**kwargs_mrl)
    mrl_table = maintenanceItemTable(mrl_filter)

    #Filter for maintenance item by ship excluding mrl.
    mi_filter = maintenanceItem.objects.filter(**kwargs_si).exclude(**kwargs_mrl)
    mi_table = maintenanceItemTable(mi_filter)


    return render(request,
        'apm/ship_instance_view.html',
        context = {
            'product_lines': product_lines,
            'ship_string': str(ship_instance_filter),
            'ship_instance': ship_instance_filter,
            'mrl_table': mrl_table,
            'mi_table': mi_table,
            }
        )

def maintenance_item_view(request,title):
    """View Function for Product Lines"""
    product_lines = productLine.objects.all()
    mi = maintenanceItem.objects.get(title=title)
    kwargs_mi = {'maintenanceItem':mi}
    table = supplyPartTable(supplyPart.objects.filter(**kwargs_mi))

    return render(request,
        'apm/maintenance_item_view.html',
        context = {
        'product_lines': product_lines,
        'maintenance_item': mi,
        'table': table,
        }
        )
