from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField

from .models import *


class Add_Card_Product_forms(forms.ModelForm):
    class Meta:
        model = Card_Product
        fields =  {'Product_photo', 'Product_name', 'Product_description', 'Product_price', 'Product_published', 'Slug', 'Category_id'}
        widgets = {
            'Product_description' : forms.Textarea(attrs={'cols' : 45, 'rows' : 8}),

        }
    

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'my-field-pink-reg'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'my-field-blue-reg'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'my-field-pink-reg'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'my-field-blue-reg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'my-field-pink-reg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'my-field-blue-reg'}))
    class Meta:
        model = Users
        fields = {'first_name', 'last_name', 'username', 'email', 'password1', 'password2', }
    


class LoginUserForm(AuthenticationForm):
    class Meta:
        models = Users
        fields = {'username', 'password'}



class ContactUserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':14}))
    captcha = CaptchaField()


class ProfilUserForm(UserChangeForm):
    user_photo = forms.ImageField(widget=forms.FileInput(attrs={'class':'my_user_photo_field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'my-field-blue'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'my-field-pink'}))
    class Meta:
        model = Users
        fields = {'first_name', 'last_name', 'user_photo', 'username', 'email', }
        
