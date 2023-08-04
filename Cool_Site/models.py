from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser



class Card_Product(models.Model):
    Product_photo = models.ImageField(upload_to='images/', blank=True)
    Product_name = models.CharField(max_length=30)
    Product_description = models.TextField(max_length=100)
    Product_created_time = models.DateTimeField(auto_now_add=True)
    Product_last_update = models.DateTimeField(auto_now=True)
    Product_published = models.BooleanField(default=True)
    Product_price = models.DecimalField(max_digits=9, decimal_places=2)
    Category_id = models.ForeignKey('Card_Category', on_delete=models.PROTECT)
    Slug = models.SlugField(max_length=30, verbose_name="URL")


    def __str__(self):
        return f" {self.Product_name} | category -> {self.Category_id}" 


    def get_absolute_url(self):
        return reverse('category', kwargs={'Category_slug': self.Slug})

class Card_Category(models.Model):
    Category_name = models.CharField(max_length=30)
    Slug = models.SlugField(max_length=30, unique=True, verbose_name="URL")


    def __str__(self):
        return self.Category_name


    def get_absolute_url(self):
        return reverse('category', kwargs={'Category_slug': self.Slug})

# -----------------------------------------------------------------------------------------------

class Users(AbstractUser):
    birth_day = models.DateField(blank=True, null=True)
    user_photo = models.ImageField(upload_to='Cool_Site/static/cool_site/images/user_ava', blank=True, null=True)



# -----------------------------------------------------------------------------------------------
class Basket_Query_Set(models.QuerySet):
    def all_basket_price(self):
        total_B_price = 0
        for total_things in self:
            total_B_price+=total_things.card_quantity_sum()
        return total_B_price

    def all_busket_quantity(self):
        basket_B_quantity = 0
        for total_things in self:
            basket_B_quantity+=total_things.quantity
        return basket_B_quantity


class Card_Basket(models.Model):
    B_user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    B_product = models.ForeignKey(to=Card_Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    objects = Basket_Query_Set.as_manager()

    def card_quantity_sum(self):
        return self.B_product.Product_price * self.quantity

