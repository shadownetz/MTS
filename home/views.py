from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate


def home_index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        new_user = User(
            email=request.POST['email'],
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            avatar=request.FILES['avatar']
        )
        if User.objects.filter(is_staff=True).count() <= 0:
            new_user.is_staff = True
        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('login')
    return render(request, 'home/signup.html')


def mts_login(request):
    response = {
        'error': False,
        'message': 'Invalid Email or Password'
    }
    if request.method == 'POST':
        next_url = request.POST['next']
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('dashboard:index')
        else:
            response['error'] = True
    return render(request, 'home/login.html', response)
