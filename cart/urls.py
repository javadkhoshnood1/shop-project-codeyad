from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.CartProductView.as_view(), name="cart_product"),
    path("add/<int:id>", views.CartAddProductView.as_view(), name="add_product"),
    path("delete/<int:id>", views.CartDeleteView.as_view(), name="delete_product"),
    path("chackout/", views.ChackOut.as_view(), name="cart_chackout"),
    path("data/kharid", views.DataKharidView.as_view(), name="data_kharid"),
    path("data/useraddress", views.DataUserAdderssView.as_view(), name="data_user_address"),
    path("add/order/useraddress",views.AddOrderAddress.as_view(),name="add_order_address"),
    path("delete/cart", views.DeleteCartView.as_view(), name="deletecart")

]
