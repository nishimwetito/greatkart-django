from django.shortcuts import render

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

    return cart
def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)

def cart(request):
    return render(request,'store/cart.html')