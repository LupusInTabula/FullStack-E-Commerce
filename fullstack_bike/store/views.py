from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Store


def store(request):
    stores = Store.objects.all()
    return render(request, 'store/bikestore.html', {'stores': stores})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, email, password, password2]):
            messages.info(request, 'All fields are required')
            return redirect('register')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'store/register.html', {'register': register})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/store/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'store/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/store/')
