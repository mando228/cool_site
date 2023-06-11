from django.contrib import admin

from .models import *


# вспомогательные классы
class Card_Product_Admin(admin.ModelAdmin):
    list_display = ('id', 'Product_photo', 'Product_name', 'Product_created_time', 'Product_published')


class Card_Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'Category_name')
    prepopulated_fields = {"Slug" : ("Category_name",)}


# ---------------------------------------------------
# основные админки
admin.site.register(Card_Product, Card_Product_Admin)

admin.site.register(Card_Category, Card_Category_Admin)

