from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Single Project to Multiple Application

def One(request):
    print("First Applicaton")
    return HttpResponse("<h1 style=text-align:center;>FIRST PAGE DISPLAYED</h1>")