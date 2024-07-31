from django.db import models

# Create your models here.
from django.utils.html import format_html
from jalali_date import datetime2jalali, date2jalali

from accounts.models import User


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name="رنگ محصول")

    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها "

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.IntegerField(verbose_name="سایز محصول")

    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایز"

    def __str__(self):
        return str(self.size)


Choise_quality_product = (
    ('دارای تضمین اصالت کالا', " دارای تضمین اصالت کالا"),
    (' تضمین اصالت کالا ندارد ', " تضمین اصالت کالا ندارد "),

)


class Category(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="دسته بندی پدر")
    slug = models.SlugField(null=True, blank=True, verbose_name="کد ")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="اسم سته بندی")
    body = models.TextField(null=True, blank=True, verbose_name="توضیحات دسته بندی")
    image = models.ImageField(null=True, blank=True, upload_to="category_image", verbose_name="عکس دسته بندی")
    created_at = models.DateTimeField(null=True, auto_now_add=True, blank=True, verbose_name="تاریخ اضافه شدن ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها "

    def Created_at(self):
        return date2jalali(self.created_at)


class Product(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="نام محصول")
    image = models.ImageField(upload_to="productimage", null=True, blank=True, verbose_name="عکس محصول")
    price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="قیمت محصول")
    size = models.ManyToManyField(Size, verbose_name="سایز محصول")
    color = models.ManyToManyField(Color, verbose_name="رنگ محصول")
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


class InformationProduct(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name="informatin",
                                verbose_name="محصول")
    text = models.TextField()

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات ها"

    def __str__(self):
        return self.text[:30]
