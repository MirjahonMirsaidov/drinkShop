# Generated by Django 3.2.4 on 2021-06-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210612_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_en',
            field=models.SlugField(default='', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_ru',
            field=models.SlugField(default='', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_uz',
            field=models.SlugField(default='', editable=False, null=True),
        ),
    ]