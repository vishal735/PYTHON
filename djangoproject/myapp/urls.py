from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('blogdetails',blogdetails,name='blogdetails'),
    path('blog',blog,name='blog'),
    path('checkout',checkout,name='checkout'),
    path('contact',contact,name='contact'),
    path('shop',shop,name='shop'),
    path('shopdetails',shopdetails,name='shopdetails'),
    path('shoppingcart',shoppingcart,name='shoppingcart'),
    
    
    
    
]
