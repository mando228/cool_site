from typing import Any, Dict

from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormView

from .models import *
from .forms import *


class Face_Page_View(ListView):
    model = Card_Product
    template_name = 'face_page.html'



class Home_Page_View(ListView):
    paginate_by = 3
    model = Card_Product
    template_name = 'home_page.html'
    context_object_name = 'product_card_list'


    def get_queryset(self):
         return Card_Product.objects.filter(Product_published=True)



class Show_Category_View(ListView):
    paginate_by = 3
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



# пагинация

def Paginate_View(request):
    contact_list = Card_Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home_page.html', {'page_obj' : page_obj})
# ---------------------------------------------------------------------

# создает  акк
class Register_User_View(CreateView):
    model = Users
    form_class = RegisterUserForm
    template_name = 'users/register_page.html'
    success_url = reverse_lazy('login-page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login-page')

# вход в акк
class Login_User_View(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login_page.html'


    def get_success_url(self):
        return reverse_lazy('face-page')

# выход с акк
def Logout_User(request):
    logout(request)
    return redirect('face-page')


class Contact_User_View(FormView):
    form_class = ContactUserForm
    template_name = 'users/contact_page.html'
    success_url = reverse_lazy('face-page')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home-page')


class Profil_User_View(UpdateView):
    model = Users
    form_class = ProfilUserForm
    template_name = 'users/profile_page.html'  

    # эт чобы можно было сохранить изменения профиля
    def get_success_url(self):
        return reverse_lazy('profile-page', args=(self.object.id, ))

    def get_context_data(self, **kwargs):
        context =  super(Profil_User_View, self).get_context_data(**kwargs)
        context['basket_product'] = Card_Basket.objects.filter(B_user=self.object)
        return context
    

def Add_Basket_View(request, product_id):
    bought_product = Card_Product.objects.get(id=product_id)
    baskets = Card_Basket.objects.filter(B_user=request.user, B_product=bought_product)

    if not baskets.exists():
        Card_Basket.objects.create(B_user=request.user, B_product=bought_product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def Delete_Basket_View(request, basket_id):
    baskets = Card_Basket.objects.get(id=basket_id)
    baskets.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])