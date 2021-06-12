from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Brand)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', )

