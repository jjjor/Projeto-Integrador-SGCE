from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def profile_prof(request):
    return render(request, 'profile-prof.html')

def infos_security(request):
    return render(request, 'infos-security.html')

def info_pessoal(request):
    return render(request, "info-pessoal.html")