from django.shortcuts import render
from .forms import SearchProductHome
# Create your views here.
from django.views.generic import ArchiveIndexView

from product.models import Attributes, Product, Category


def homepageview(request):
    form = SearchProductHome()
    all_attributes = Attributes.objects.all()
    all_product = Product.objects.all()[0:4]
    product = Product.objects.all()
    last_product = Product.objects.all().order_by("-created_at")[0:4]
    all_category = Category.objects.all()[0:3]


    return render(request, "home/index.html",
                  {"attributes": all_attributes, "products": all_product, "categorys": all_category,
                   "last_product": last_product ,"product" : product ,"form":form})
