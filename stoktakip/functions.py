from math import prod
from .models import *
from django.shortcuts import render


def getProductIdList(storeProduct):
    
    idList = []
    
    for product in storeProduct:
    
        for aProduct in product.salesProducts.all():
    
            idList.append(aProduct.id)

    return idList


def saleProductStock(productList):
    
    for id in productList:
        
        productObject = Product.objects.get(id=id)
        countStock  = productObject.countStock - 1
        productName = productObject.productName 
        
        Product.objects.filter(productName=productName).update(countStock=countStock)


def addSalesList(product):

    saleProduct = SalesProducts(
        storeName      = product.storeName,
        salesProductId = product.salesProductId,
        salesProducts  = product.salesProducts,
        storeStock     = product.storeStock
    )

    saleProduct.save()


def updateProductStockAndBundle(id,newStock):

    if newStock == 0:

        InStoreProducts.objects.filter(salesProducts=id).update(countStock=0)

    else:

        productObject = Product.objects.get(id=id)
        productObject.countStock  = newStock
        productObject.save()

        inStoreProductObject = InStoreProducts.objects.filter(salesProducts=productObject.id)

        for product in inStoreProductObject:

            updateBundle(product.salesProductId)

            


def updateBundle(id):


    inStoreProductObject = InStoreProducts.objects.filter(salesProductId=id)

    productList = getProductIdList(inStoreProductObject)

    stockList = []

    for id in productList:
            
        productObject = Product.objects.get(id=id)

        stockList.append(productObject.countStock)


    InStoreProducts.objects.filter(salesProducts=id).update(storeStock=min(stockList))








            











        




        

