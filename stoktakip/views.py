from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from .functions import *
from .forms import *
# Create your views here.


def index(request):
    
    products = Product.objects.all()

    context = { 'products':products }

    return render(request,"index.html",context)


def bundleProduct(request):

    bundle = InStoreProducts.objects.all()

    context = { 'bundle' : bundle }

    return render(request,"bundle.html",context)


def saleProduct(request,salesProductId):       

    storeProduct = InStoreProducts.objects.filter(salesProductId=salesProductId)

    productList = getProductIdList(storeProduct)

    saleProductStock(productList)
    updateBundle(salesProductId)

    return redirect("index")


def addProduct(request):

    productForm = ProductForm()

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():
            
            productName = form.cleaned_data["productName"]
            countStock  = form.cleaned_data["countStock"]
            
            Product.objects.filter(productName=productName).update(countStock=countStock)

            form.save()

            return redirect("index")
            
    context = {"productForm":productForm}


    return render(request,"newProduct.html",context)


def addBundle(request):

    bundleForm = InStoreProductsForm()

    if request.method == "POST":

        form = InStoreProductsForm(request.POST)


        if form.is_valid():

            form.save()
            return redirect("index")

        else:

            context = {"errorCode" : 406 , 'errorTitle' : 'Stok Hatası', 'errorDescription' : 'Girdiğiniz Stok Sayısı Ürün Stoğundan fazla'}
            return render(request,"error.html",context)


    context = {"bundleForm":bundleForm}

    return render(request,"addBundle.html",context)


def deleteProduct(request,id):

    productObject = Product.objects.get(id=id)
    productName   = productObject.productName

    InStoreProducts.objects.filter(salesProducts=id).delete()
    Product.objects.filter(productName=productName).delete()

    return redirect("index")


def deleteInStoreProducts(request,id):
    
    InStoreProducts.objects.filter(id=id).delete()

    return redirect("index")


def updateProductStock(request,id):

    product = Product.objects.get(id=id)
    
    if request.method == "POST":

        newStock = request.POST.get('stock')
        updateProductStockAndBundle(id,newStock)

        return redirect("index")

    context = {"product":product}

    return render(request,"editProduct.html",context)


def updateBundleStock(request,id):

    bundle = InStoreProducts.objects.get(salesProductId=id)

    print(id)

    if request.method == "POST":

        newStock = request.POST.get('stock')

        updateBundle(id,newStock)

        return redirect("bundle")

    context = {"bundle":bundle}

    return render(request,"editBundle.html",context)




