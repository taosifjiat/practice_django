from django.shortcuts import render
from .models import Product
# Create your views here.
def my_product(request):
    product=Product.objects.all()
    context={"product":product}
    return render(request,'dokan/myproduct.html',context)
def product_detail(request,id):
    p=Product.objects.get(id=id)
    context={'product':p}
    return render(request,'product-detail.html',context)