from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.generic import ListView, CreateView

from .models import *
from .forms import *


class Face_Page_View(ListView):
    model = Card_Product
    template_name = 'face_page.html'




class Home_Page_View(ListView):
    model = Card_Product
    template_name = 'home_page.html'
    context_object_name = 'product_card_list'


    def get_queryset(self):
         return Card_Product.objects.filter(Product_published=True)




class Show_Category_View(ListView):
    model = Card_Product
    template_name = 'home_page.html'
    context_object_name = 'product_card_list'
    allow_empty = True

    def get_queryset(self):
        return Card_Product.objects.filter(Category_id__Slug=self.kwargs['Category_slug'], Product_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['product_card_list'][0].Category_id
        return context




class Add_Card_Product_View(CreateView):
    form_class = Add_Card_Product_forms
    template_name = 'Add_Product.html'



















