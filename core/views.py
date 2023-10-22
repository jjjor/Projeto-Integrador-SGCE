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

def info_security(request):
    return render(request, 'info-security.html')

def info_pessoal(request):
    return render(request, 'info-pessoal.html')

def report_bug(request):
    return render(request, 'report-bug.html')

def matches(request):
    return render(request, 'matches.html')

def report_bug(request):
    return render(request, "report-bug.html")
