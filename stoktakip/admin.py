from django.contrib import admin
from .models import Product,Store,InStoreProducts
from django.utils.safestring import mark_safe

# Register your models here.

class InStoreProductsAdmin(admin.ModelAdmin):
    
    list_display = ("storeName","salesProductId","storeStock","selected_salesProducts",)

    def selected_salesProducts(self,obj):

        html = ""

        for salesProduct in obj.salesProducts.all():
            html += salesProduct.productName + "<br>"


        return mark_safe(html)


class SalesProduct(admin.ModelAdmin):
    
    list_display = ("storeName","salesProductId","storeStock","selected_salesProducts",)

    def selected_salesProducts(self,obj):

        html = ""

        for salesProduct in obj.salesProducts.all():
            html += salesProduct.productName + "<br>"


        return mark_safe(html)



class ProductAdmin(admin.ModelAdmin):
    list_display = ("productName","countStock")

admin.site.register(Product,ProductAdmin)
admin.site.register(Store)
admin.site.register(InStoreProducts,InStoreProductsAdmin)


