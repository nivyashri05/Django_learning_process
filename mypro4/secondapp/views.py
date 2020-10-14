from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Second(request):
    print("Second Applicaton")
    return HttpResponse("<h1 style=text-align:center;>SECOND PAGE DISPLAYED</h1>")