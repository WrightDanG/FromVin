from django.contrib import admin
from .models import Product, Category, TastingProfile

# Register product aspects to be controlled
# within the admin portal


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'tastingprofile',
    )

    ordering = ('category', 'sku',)

# Register categories


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register tasting profiles for Recommend app


class TastingProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TastingProfile, TastingProfileAdmin)
