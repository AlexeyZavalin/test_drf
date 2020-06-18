from django.contrib import admin
from products.models import Category, Product, PaymentType, Kitchen, Establishment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title', )


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    pass


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass
