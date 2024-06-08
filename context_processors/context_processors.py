from product.models import Product,Category


def category(request):
    list_category = Category.objects.all()
    return {"list_category" : list_category }