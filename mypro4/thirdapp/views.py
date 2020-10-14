from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Third(request):
    print("Third Applicaton")
    return HttpResponse("<h1 style=text-align:center;>THIRD PAGE DISPLAYED</h1>")