from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Defining urls at application level

def first_view(request):
    return HttpResponse("<center><h1 style=color:red>  Response from 1st view </h1></center>")

def second_view(request):
    return HttpResponse("<center><h1 style=color:aqua> Response from 2nd view </h1></center>")

def third_view(request):
    return HttpResponse("<center><h1 style=color:pink> Response from 3rd view </h1></center>")

def fourth_view(request):
    return HttpResponse("<center><h1 style=color:green> Response from 4th view </h1></center>")