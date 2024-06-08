# Generated by Django 5.0.3 on 2024-06-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quality',
            field=models.CharField(blank=True, choices=[('دارای تضمین اصالت کالا', ' دارای تضمین اصالت کالا'), (' تضمین اصالت کالا ندارد ', ' تضمین اصالت کالا ندارد ')], max_length=24, null=True, verbose_name='کیفیت محصول'),
        ),
    ]
