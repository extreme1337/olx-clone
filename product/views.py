from django.shortcuts import render
from .models import Product

# Create your views here.
def productlist(request):
    productlist = Product.objects.all()

    context = {
        'product_list': productlist
    }

    template = 'product/product_list.html'

    return render(request, template, context)


def productdetail(request, id):
    productdetail = Product.objects.get(id=id)
    template = 'product/product_detail.html'
    context = {
        'product_detail': productdetail
    }

    return render(request, template, context)
