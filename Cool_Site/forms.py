from django import forms

from .models import *


class Add_Card_Product_forms(forms.ModelForm):
    class Meta:
        model = Card_Product
        fields =  {'Product_photo', 'Product_name', 'Product_description', 'Product_published', 'Slug', 'Category_id'}
        widgets = {
            'Product_description' : forms.Textarea(attrs={'cols' : 45, 'rows' : 8}),

        }
    



