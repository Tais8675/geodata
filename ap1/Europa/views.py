from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def europa(request):
    return render(request, "europa.html")

def frança(request):
    return render(request, "frança.html")

def italia(request):
    return render(request, "italia.html")

def suecia(request):
    return render(request, "suecia.html")