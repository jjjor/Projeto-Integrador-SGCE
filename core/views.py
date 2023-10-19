from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index')

def register(request):
    return render(request, 'register')

def login(request):
    return render(request, 'login.html')

