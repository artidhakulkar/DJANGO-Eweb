

from django.urls import path, include
from.import views


urlpatterns = [

    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('traker/', views.traker, name='traker'),
    path('search/', views.traker, name='traker'),
    path('productview/', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout')

]