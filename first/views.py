from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find_us.html')

def animals_view(request):
    return render(request, 'animals.html')