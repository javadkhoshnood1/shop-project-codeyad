# Generated by Django 5.0.3 on 2024-05-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_fullname_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='شماره تماس'),
        ),
    ]
