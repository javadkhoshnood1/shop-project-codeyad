# Generated by Django 5.0.3 on 2024-07-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_informationproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ اضافه شدن '),
        ),
    ]
