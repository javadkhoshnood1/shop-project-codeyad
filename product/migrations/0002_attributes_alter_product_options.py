# Generated by Django 5.0.3 on 2024-05-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان ویژگی ها ')),
                ('body', models.TextField(blank=True, null=True, verbose_name='تضیحات ویژگی ها')),
            ],
            options={
                'verbose_name': 'ویژگی',
                'verbose_name_plural': 'ویژگی ها ',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]
