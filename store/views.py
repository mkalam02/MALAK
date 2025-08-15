from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/home.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('home')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for id, qty in cart.items():
        product = Product.objects.get(id=id)
        item_total = product.price * qty
        total += item_total
        cart_items.append({'product': product, 'qty': qty, 'item_total': item_total})
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})