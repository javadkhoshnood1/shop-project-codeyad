from django.contrib import admin

# Register your models here.
from product.models import Product, Attributes, Comment, Category


@admin.register(Product)
class ProductRegister(admin.ModelAdmin):
    list_display = ("name", "color", "price")
    search_fields = ("name", "price")


@admin.register(Attributes)
class AttributesRegister(admin.ModelAdmin):
    list_display = ("title", "body")
    search_fields = ("title", "body")


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    list_display = ("name", "body")
    search_fields = ("name", "body")


@admin.register(Comment)
class CommentRegister(admin.ModelAdmin):
    list_display = ("user", "body", "product")
    search_fields = ("body",)
