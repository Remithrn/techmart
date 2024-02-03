from django.urls import path
from . import views
app_name="shop"

urlpatterns=[
    path("",views.home,name="home"),
    path("products/",views.ProductList.as_view(),name="products"),
    path("product/<str:slug>",views.ProductDetail.as_view(),name="detail")
]