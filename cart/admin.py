from django.contrib import admin

# Register your models here.
from cart import models


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItems


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid")
    list_filter = ("is_paid",)
    inlines = (OrderItemAdmin,)


@admin.register(models.DiscountCodeApply)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ("name", "discount", "quantity")
