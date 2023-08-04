from django.urls import path


from .views import *

urlpatterns = [
    path('', Face_Page_View.as_view(), name='face-page'),
    path('home/', Home_Page_View.as_view(), name='home-page'),
    path('category/<slug:Category_slug>/', Show_Category_View.as_view(), name='category'),
    path('add/', Add_Card_Product_View.as_view(), name='add_product_card-page'),
    path('registration/', Register_User_View.as_view(), name='register-page'),
    path('login/', Login_User_View.as_view(), name='login-page'),
    path('logout/', Logout_User, name='logout'),
    path('contact/', Contact_User_View.as_view(), name='contact-page'),
    path('profile/<int:pk>/', Profil_User_View.as_view(), name='profile-page'),
    path('baskets/add/<int:product_id>/', Add_Basket_View, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', Delete_Basket_View, name='basket_del'),


]

