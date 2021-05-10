from django.http import HttpResponse
from django.shortcuts import render

def Main(request):
    return render(request, 'Main.html')

def Contact(request):
    return render(request, 'Contact.html')

def About(request):
    return render(request, 'About.html')