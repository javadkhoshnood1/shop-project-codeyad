from django.db import models

# Create your models here.
from accounts.models import User, UserAddress
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_activate")

    is_paid = models.BooleanField(default=False, verbose_name="بررسی پرداخت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ سفارش ")
    total_price = models.BigIntegerField(default=0, verbose_name="قیمت کل محصولات خرید کرده")

    class Meta:
        verbose_name = "سفارش کاربر"
        verbose_name_plural = "سفارش ها ثبت شده"


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    tedad = models.IntegerField(default=0, verbose_name="تعداد محصول")
    price = models.BigIntegerField(default=0, verbose_name="قیمت محصول")
    total = models.BigIntegerField(default=0, verbose_name="قیمت نهایی")
    size = models.CharField(max_length=2, verbose_name="سایز سفارش")
    color = models.CharField(max_length=12, verbose_name="رنگ")

    class Meta:
        verbose_name = "ایتم سفارش"
        verbose_name_plural = "ایتم های سفارش"


class DiscountCodeApply(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام تخفیف")
    discount = models.SmallIntegerField(default=0, verbose_name="درضد")
    quantity = models.SmallIntegerField(default=5, verbose_name="تعداد")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیف ها "
