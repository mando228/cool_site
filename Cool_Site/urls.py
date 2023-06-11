from django.urls import path


from .views import *

urlpatterns = [
    path('', Face_Page_View.as_view()),
    path('home/', Home_Page_View.as_view(), name='home-page'),
    path('category/<slug:Category_slug>/', Show_Category_View.as_view(), name='category'),# здесь формируется URL-адрес | Category_slug => крючок
                                                            # этот крючок соеденяет Card_Product и Card_Category

    path('add/', Add_Card_Product_View.as_view(), name='add_product_card-page'),

]

