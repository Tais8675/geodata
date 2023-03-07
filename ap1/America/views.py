from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def america(request):
    return render(request, "america.html")

def canada(request):
    return render(request, "canada.html")

def mexico(request):
    return render(request, "mexico.html")