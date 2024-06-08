from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from product.models import Product, Category


class ProductList_Category_View(DetailView):
    model = Category
    template_name = "product/product_shop.html"
    context_object_name = "category_detail"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(ProductList_Category_View, self).get_context_data()
        category_detail = Category.objects.get(id=self.kwargs["id"])
        context["products"] = category_detail.product_set.all()
        context["list_category"] = Category.objects.all()
        context["category_name"] = category_detail.name
        return context


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 6
    template_name = "product/product_shop.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_category"] = Category.objects.all()

        return context

class ProductDetailView(DetailView):
    pk_url_kwarg = "id"
    model = Product
    context_object_name = "product"
    template_name = "product/product_detail.html"


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context["related_product"] = Product.objects.all()[0:3]
        return context