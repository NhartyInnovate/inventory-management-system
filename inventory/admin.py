from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(InventoryItem)
admin.site.register(StockTransaction)
admin.site.register(AssetAssignment)
admin.site.register(AuditLog)