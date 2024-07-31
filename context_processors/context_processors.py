from cart.models import Order
from product.models import Category, Product


def categoryss(request):
    categoryss = Category.objects.filter(parent=None)
    return {"categoryss": categoryss}

#
#
# def count_cart(request):
#     if request.user.is_authenticated:
#         order = Order.objects.get(user=request.user)
#         count_cart = order.orderitems_set.count()
#         return {"count_cart" : count_cart}
#     else:
#         return {}



def products_sidbar_discount(request):
    products_sidbar_discount = Product.objects.filter(color__name__in=["black",])[0:3]

    return {"products_sidbar_discount" :products_sidbar_discount , }
