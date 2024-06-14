# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from store.models import Store
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Store, id=product_id)
    if product.stock <= 0:
        messages.error(request, 'This item is out of stock')
        return redirect('store:store')

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        if product.stock > 0:
            cart_item.quantity += 1
            cart_item.save()
    else:
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
    return redirect('store:store')


@login_required
def confirm_order(request):
    total_price = 0
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.cartitem_set.all()

        if not cart_items.exists():
            messages.error(request, 'Empty cart')
            return redirect('store:store')

        for cart_item in cart_items:
            product = cart_item.product
            if product.stock < cart_item.quantity:
                messages.error(request, f"This item : {product.name} is out of stock")
                return redirect('store:store')

            product.stock -= cart_item.quantity
            product.save()

            i = product.price * cart_item.quantity
            total_price = float(i + total_price)

        cart_items.delete()
        messages.success(request, 'Order confirmed and items has been removed from the cart. '
                                  'Total price: $' + str(total_price))
        return redirect('store:store')
    else:
        return redirect('cart:cart_detail')
