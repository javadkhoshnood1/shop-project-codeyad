from django.contrib import admin
from . import models
# Register your models here.
from product.models import Product, Attributes, Comment, Category, Color, Size


class InformationProduct(admin.StackedInline):
    model = models.InformationProduct


@admin.register(Product)
class ProductRegister(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name", "price")
    inlines = (InformationProduct,)


@admin.register(Attributes)
class AttributesRegister(admin.ModelAdmin):
    list_display = ("title", "body")
    search_fields = ("title", "body")


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    list_display = ("name", "body","parent","slug")
    search_fields = ("name", "body")
    prepopulated_fields = {"slug": ("name",),}


@admin.register(Comment)
class CommentRegister(admin.ModelAdmin):
    list_display = ("user", "body", "product")
    search_fields = ("body",)


admin.site.register(Color)
admin.site.register(Size)
