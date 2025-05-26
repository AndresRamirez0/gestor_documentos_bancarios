from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Usuario o contraseña incorrectos'
    return render(request, 'core/login.html', {'error': error})

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def upload(request):
    return render(request, 'core/upload.html')

@login_required
def search_docs(request):
    return render(request, 'core/search.html')

@login_required
def reports(request):
    return render(request, 'core/reports.html')

@login_required
def admin_users(request):
    return render(request, 'core/admin_users.html')

def logout_view(request):
    logout(request)
    return redirect('login')
