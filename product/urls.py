from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("list/",views.ProductListView.as_view(),name="product_list"),
    path("list/category/<int:id>/",views.ProductList_Category_View.as_view(),name="product_list_c"),
    path('detail/<int:id>/',views.ProductDetailView.as_view(),name="product_detail")

]
