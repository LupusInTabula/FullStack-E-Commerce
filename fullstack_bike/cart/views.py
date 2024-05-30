from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from store.models import Store
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Store, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('store:store')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:cart_detail')
