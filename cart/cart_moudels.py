from product.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = request.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Product.objects.get(id=int(item["id"]))
            item["product"] = product
            item["total"] = int(item["price"]) * int(item["tedad"])
            item["uniqe"] = self.genertor_uniqe_url(product.id, item["size"])
            yield item

    def genertor_uniqe_url(self, id, size):
        result = f"{id}{size}"
        return result

    def add(self, product, tedad, color, size):
        uniqe_product = self.genertor_uniqe_url(product.id, size)
        if uniqe_product not in self.cart:
            self.cart[uniqe_product] = {"tedad": 0, "color": color, "price": str(product.price), "size": size,
                                        "id": str(product.id)}

        self.cart[uniqe_product]["tedad"] += int(tedad)
        self.session.modified = True

    def delete(self, id):
        print(self.cart.keys())
        print(id)
        if str(id) in self.cart:
            del self.cart[str(id)]
            self.session.modified = True

    def remove_cart(self):
        self.cart.popitem()
        self.session.modified = True
