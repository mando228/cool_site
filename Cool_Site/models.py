from django.db import models
from django.urls import reverse



class Card_Product(models.Model):
    Product_photo = models.ImageField(upload_to='images/', blank=True)
    Product_name = models.CharField(max_length=30)
    Product_description = models.TextField(max_length=100)
    Product_created_time = models.DateTimeField(auto_now_add=True)
    Product_last_update = models.DateTimeField(auto_now=True)
    Product_published = models.BooleanField(default=True)
    Category_id = models.ForeignKey('Card_Category', on_delete=models.PROTECT)# крючок для распознавания категории
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
                #     как будет           крючок адреса,   и это чтобы 
                # формироваться         чтобы показывала      страница показывала
                # начало адреса       нужную Card_Product     текущую кате-
                #                                               горию в URL