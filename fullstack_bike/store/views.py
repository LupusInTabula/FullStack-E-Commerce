from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Store


def store(request):
    stores = Store.objects.all().order_by('name')
    return render(request, 'store/MainStore.html', {'stores': stores})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, email, password, password2]):
            messages.info(request, 'All fields are required')
            return redirect('store:register')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('store:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered')
                return redirect('store:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('store:login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('store:register')
    return render(request, 'store/register.html', {'register': register})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('store:store')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('store:login')
    return render(request, 'store/login.html', {'login': login})


def logout(request):
    auth.logout(request)
    return redirect('store:store')


def search(request):
    query = request.GET.get('q')
    print(f"Search query: {query}")
    if query:
        storesearch = Store.objects.filter(name__icontains=query)
        print(f"Stores found: {storesearch}")
    else:
        storesearch = Store.objects.all()
    return render(request, 'store/search_result.html', {'storesearch': storesearch})
