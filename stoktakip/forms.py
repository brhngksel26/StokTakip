from .models import *
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = ["productName","countStock"]

    
class InStoreProductsForm(forms.ModelForm):

    class Meta:

        model = InStoreProducts
        fields = ["storeName","salesProductId","salesProducts","storeStock"]
        exclude = ['Product','Store']

    def clean_storeStock(self):

        salesProduct = self.cleaned_data.get("salesProducts")
        storeStock   = self.cleaned_data.get("storeStock")

        for product in salesProduct:

            if storeStock > product.countStock:
        
                raise forms.ValidationError(u'Ürün stoğundan fazla satış stoğu girilemez')

        return storeStock

        
