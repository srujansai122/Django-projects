from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<slug:slug>/",views.detail,name='detail'),
    path("cart/add",views.add_to_cart,name='add_to_cart')
]