from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count


# Create your views here.
def productlist(request):
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))

    paginator = Paginator(productlist, 10)

    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {
        'product_list': productlist,
        'category_list': categorylist
    }

    template = 'product/product_list.html'

    return render(request, template, context)


def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'product/product_detail.html'
    context = {
        'product_detail': productdetail,
        'product_images': productimages
    }

    return render(request, template, context)
