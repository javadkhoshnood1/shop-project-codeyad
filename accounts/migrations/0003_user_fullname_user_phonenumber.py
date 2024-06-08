# Generated by Django 5.0.3 on 2024-05-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options_remove_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
