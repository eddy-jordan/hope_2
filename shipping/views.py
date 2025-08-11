from django.shortcuts import render, get_object_or_404
from .models import Package

def track_package(request, tracking_id):
    package = get_object_or_404(Package, tracking_id=tracking_id)
    return render(request, 'shipping/track.html', {'package': package})

from django.shortcuts import render

def index(request):
    return render(request, 'shipping/index.html')  # Make sure this template exists


from django.shortcuts import redirect

def track_redirect(request):
    tracking_id = request.GET.get('tracking_id')
    if tracking_id:
        return redirect('track_package', tracking_id=tracking_id)
    else:
        return redirect('index')


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shipping/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'shipping/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
