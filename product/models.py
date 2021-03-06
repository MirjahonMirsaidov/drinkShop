from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', editable=False)
    price = models.FloatField()
    size = models.CharField(max_length=255)
    stock_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        super(Product, self).save()
        if not self.slug:
            slug = slugify(self.title)
            try:
                post_obj = Product.objects.filter(slug=slug).first()
                slug += str(self.id)
            except Product.DoesNotExist:
                pass
            self.slug = slug
            self.save()

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return self.product.title

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

