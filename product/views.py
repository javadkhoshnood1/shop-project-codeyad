from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView

from home.forms import SearchProductHome
from product.models import Product, Category


class ProductSearchHomePage(ListView):
    def post(self, request):
        form = SearchProductHome(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category = Category.objects.all()
            products = Product.objects.filter(name__contains=data["name"])
            return render(request, "product/product_shop.html",
                          {"name_search": data["name"], "products": products, "form": form, "list_category": category})

        print("form nnotttt ok")
        return render(request, "product/product_shop.html", {"form": form})


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
        context["form"] = SearchProductHome()

        return context


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = "products"
    template_name = "product/product_shop.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        queryset = Product.objects.all()
        paginatorr = Paginator(queryset, 5)
        page_number = request.GET.get("page")
        if page_number:
            sett = paginatorr.get_page(page_number)
        else:
            sett = paginatorr.get_page(1)
        sizes = request.GET.getlist("sizes")
        colors = request.GET.getlist("colors")
        min_price = request.GET.get("min-price")
        max_price = request.GET.get("max-price")
        print(sizes, colors, min_price, max_price)

        if colors:
            queryset = queryset.filter(color__name__in=colors)
            print(sett)

        if sizes:
            queryset = queryset.filter(size__size__in=sizes).distinct()
            print("size ok ")



        if max_price and min_price :
            if max_price == "0":
                max_price= 10000000000000
                queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
                print("price 11 ok")
            else:
                queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
                print("price ok ")
        context["list_category"] = Category.objects.all()
        context["products"] = queryset
        context["form"] = SearchProductHome()
        return context


# class ProductDetailView(DetailView):
#     pk_url_kwarg = "id"
#     model = Product
#     context_object_name = "product"
#     template_name = "product/product_detail.html"
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data()
#         context["related_product"] = Product.objects.all()[0:3]
#         return context





class ProductDetailView(DetailView):
    pk_url_kwarg = "id"
    context_object_name = "product"
    template_name = "product/product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context["related_product"] = Product.objects.all()[0:3]
        return context
