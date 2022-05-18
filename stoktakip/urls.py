from . import views
from django.urls import path

urlpatterns = [
    
        
    path('',views.index,name="index"),
    path('bundle',views.bundleProduct,name="bundle"),
    path('saleProduct/<int:salesProductId>/',views.saleProduct),
    path('addProduct',views.addProduct,name="addProduct"),
    path('addBundle',views.addBundle,name="addBundle"),
    path('deleteProduct/<int:id>/',views.deleteProduct,name="deleteProduct"),
    path('deleteInStoreProducts/<int:id>/',views.deleteInStoreProducts,name="deleteInStoreProducts"),
    path('updateProductStock/<int:id>/',views.updateProductStock,name="updateProductStock"),
    path('updateBundleStock/<int:id>',views.updateBundleStock,name="updateBundleStock" )


]