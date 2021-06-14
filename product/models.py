from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    description = models.TextField(verbose_name=_('description'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(default='', editable=False)
    price = models.FloatField(verbose_name=_('price'))
    size = models.CharField(verbose_name=_('size'), max_length=255)
    stock_count = models.PositiveIntegerField(verbose_name=_('stock_count'))
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

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(verbose_name=_('image'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))

    def __str__(self):
        return self.product.title

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True



