from django.contrib import admin
from .models import productLine,shipClass,shipInstance,maintenanceItem
from .models import maintenanceRequirementList, supplyPart
# Register your models here.
admin.site.register(productLine)
admin.site.register(shipClass)
admin.site.register(shipInstance)
admin.site.register(maintenanceItem)
admin.site.register(maintenanceRequirementList)
admin.site.register(supplyPart)
