# Generated by Django 5.0.3 on 2024-06-11 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_size_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='name',
            new_name='size',
        ),
    ]
