from django.db import models

# Create your models here.
from django.utils.html import format_html
from jalali_date import datetime2jalali, date2jalali

from accounts.models import User

Choise_color_product = (
    ('ابی', "ابی"),
    ('سفید', "سفید"),
    ('سیاه', 'سیاه'),
    ('قرمز', "قرمز")

)
Choise_quality_product = (
    ('دارای تضمین اصالت کالا', " دارای تضمین اصالت کالا"),
    (' تضمین اصالت کالا ندارد ', " تضمین اصالت کالا ندارد "),

)
Choise_size_product = (
    (30, 30),
    (31, 31), (32, 32), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40),
    (41, 41), (42, 42),
    (43, 43), (44, 44), (45, 45),

)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="اسم سته بندی")
    body = models.TextField(null=True, blank=True, verbose_name="توضیحات دسته بندی")
    image = models.ImageField(null=True, blank=True, upload_to="category_image", verbose_name="عکس دسته بندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها "


class Product(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="نام محصول")
    image = models.ImageField(upload_to="productimage", null=True, blank=True, verbose_name="عکس محصول")
    price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت محصول")
    color = models.CharField(choices=Choise_color_product, max_length=4, null=True, blank=True,
                             verbose_name="رنگ محصول")
    size = models.CharField(choices=Choise_size_product,max_length=2, null=True, blank=True, verbose_name="اندازه مصحول")
    discount = models.IntegerField(default=0, null=True, blank=True, verbose_name="تخفیف محصول")
    text = models.TextField(null=True, blank=True, verbose_name="توضیحات محصول")
    created_at = models.DateField(auto_created=True, blank=True, null=True, verbose_name="تاریخ افزودن محصول")
    category = models.ManyToManyField(Category, null=True, blank=True, verbose_name="دسته بندی ها ")
    quality = models.CharField(choices=Choise_quality_product, max_length=24, blank=True, null=True,
                               verbose_name="کیفیت محصول")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def created_at_product(self):
        return date2jalali(self.created_at)


class Comment(models.Model):
    body = models.CharField(max_length=300, null=True, blank=True, verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="تاریخ انتشار نظ")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="محصول")
    reply_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name="رپلای برای کانت")

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def Created_at(self):
        return datetime2jalali(self.created_at)


class Attributes(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="عنوان ویژگی ها ")
    body = models.TextField(null=True, blank=True, verbose_name="تضیحات ویژگی ها")
    icon_html = models.CharField(max_length=300, null=True, blank=True, verbose_name="فرمت اچ تی ام ال ایکون")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها "

    def __str__(self):
        return self.title

    def Image(self):
        return format_html(self.icon_html)
