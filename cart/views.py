from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.cart_moudels import Cart
from cart.forms import CheckOutForm
from cart.models import Order, OrderItems, DiscountCodeApply
from product.models import Product
from accounts.models import UserAddress
from django. contrib import messages

class CartProductView(View):

    def get(self, request):
        cart = Cart(request)
        total_products = 0
        address_Count = UserAddress.objects.filter(user=request.user).count()
        if address_Count == 1:
            user_address = UserAddress.objects.get(user=request.user)
        else:
            user_address = None

        for item in cart:
            total_products += item["total"]
        return render(request, "cart/cart_detail.html",
                      {"cart": cart, "total": total_products, "user_address": user_address}) 


class CartAddProductView(LoginRequiredMixin, View):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        size = request.POST.get("size")
        color = request.POST.get("color")
        tedad = request.POST.get("tedad")
        cart = Cart(request)
        cart.add(product, tedad, color, size)
        messages.success(request,"product added your cart")

        return redirect("cart:cart_product")


class CartDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        print("delet ok")
        return redirect("cart:cart_product")


class ChackOut(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        total_products = 0
        for item in cart:
            total_products += item["total"]
        form = CheckOutForm()
        return render(request, "cart/check_out.html", {"form": form, "cart": cart, "total": total_products})

    def post(self, request):
        phone = request.POST.get("phone")
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        discription = request.POST.get("discription")
        UserAddress.objects.create(user=request.user, phone=phone, firstname=firstname, lastname=lastname,
                                   address=address, email=email, discription=discription)
        cart = Cart(request)
        if Order.objects.filter(user=request.user).exists():
            order = Order.objects.get(user=request.user)
            total_products = 0
            order.orderitems_set.all().delete()
            for item in cart:
                total_products += item["total"]
                order.total_price = total_products
                OrderItems.objects.create(order=order, product=item["product"], color=item["color"], size=item["size"],
                                          price=item["price"], total=item["total"], tedad=item["tedad"])

                order.save()
                messages.success(request,"user address ")

        else:
            order = Order.objects.create(user=request.user)
            total_products = 0
            for item in cart:
                total_products += item["total"]
                order.total_price = total_products
                OrderItems.objects.create(order=order, product=item["product"], color=item["color"], size=item["size"],
                                          price=item["price"], total=item["total"], tedad=item["tedad"])

                order.save()
                messages.success(request,"user address added")

        return redirect("cart:data_kharid")


class DataKharidView(LoginRequiredMixin, View):
    def get(self, request):
        user = UserAddress.objects.get(user=request.user)
        order = Order.objects.get(user=request.user)
        orderitem = order.orderitems_set.all()
        return render(request, "cart/data_kharid_user.html", {"user": user, "orderitem": orderitem, "order": order})

    def post(self, request):
        user = UserAddress.objects.get(user=request.user)
        order = Order.objects.get(user=request.user)
        cart = Cart(request)
        total_products = 0
        for item in cart:
            total_products += item["total"]
        discount = request.POST.get("discount")
        discount_object = DiscountCodeApply.objects.get(name=discount)
        total_products -= total_products * discount_object.discount / 100
        order.total_price = total_products
        order.save()
        messages.success(request,"discount applied!")

        return render(request, "cart/check_adderss.html",
                      {"user": user, "cart": order, "discount": discount_object, "discount_name": discount})


class DataUserAdderssView(LoginRequiredMixin, View):
    def get(self, request):
        user = UserAddress.objects.get(user=request.user)
        order = Order.objects.get(user=request.user)

        return render(request, "cart/check_adderss.html", {"user": user, "cart": order})

    def post(self, request):
        user = UserAddress.objects.get(user=request.user)
        order = Order.objects.get(user=request.user)
        cart = Cart(request)
        total_products = 0
        for item in cart:
            total_products += item["total"]
        discount = request.POST.get("discount")
        discount_object = DiscountCodeApply.objects.get(name=discount)
        total_products -= total_products * discount_object.discount / 100
        order.total_price = total_products
        order.save()
        messages.success(request,"discount applied!")

        return render(request, "cart/check_adderss.html", {"user": user, "cart": order, "discount": discount_object})


class AddOrderAddress(View):
    def get(self, request):
        cart = Cart(request)
        if Order.objects.filter(user=request.user).exists():
            order = Order.objects.get(user=request.user)
            total_products = 0
            order.orderitems_set.all().delete()
            for item in cart:
                total_products += item["total"]
                order.total_price = total_products
                OrderItems.objects.create(order=order, product=item["product"], color=item["color"], size=item["size"],
                                          price=item["price"], total=item["total"], tedad=item["tedad"])

                order.save()
        else:
            order = Order.objects.create(user=request.user)
            total_products = 0
            for item in cart:
                total_products += item["total"]
                order.total_price = total_products
                OrderItems.objects.create(order=order, product=item["product"], color=item["color"], size=item["size"],
                                          price=item["price"], total=item["total"], tedad=item["tedad"])

                order.save()
                messages.success(request,"product added cart")

        return redirect("cart:data_user_address")


class DeleteCartView(View):
    def get(self,request):
        cart =Cart(request)
        cart.remove_cart()
        messages.success(request,"cart cleared!")

        return redirect("Home:index")
