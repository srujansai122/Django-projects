from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import json
from .models import Product
from .cart import Cart
# Create your views here.

def index(request):
    products=Product.objects.all();
    return render(request,'foodshop/index.html',{'products':products})



def detail(request,slug):
    product=Product.objects.get(slug=slug)
    return render(request,"foodshop/detail.html",{'product':product})

# cart
def add_to_cart(request):
    cart=Cart(request)
    if request.method=="POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        product=Product.objects.get(id=product_id)
        cart.add(product,quantity)
        cart_quantity=cart.__len__()
        return JsonResponse({"cart_quantity":cart_quantity})       
    return JsonResponse({'Message':"Invalid Request"})