from django.conf.urls import url
from django.contrib import admin
from products.views import get_products, do_search

urlpatterns=[
    url(r'^$', get_products, name="productlist"),
    url(r'^search/', do_search, name="search")
    ]