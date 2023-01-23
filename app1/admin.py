from django.contrib import admin
from app1.models import Product
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('Order_date', 'Region', 'City','Category','Product','Quantity','UnitPrice' )