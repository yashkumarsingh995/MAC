from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.productView,name="ProductView"),
    path("checkout/",views.checkout,name="CheckOut"),
    path("cart/",views.cart,name="cart")
]
