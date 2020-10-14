from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# single application with multiple views

def goodmorning(request):
    return HttpResponse('<center><h1 style=color:aqua>GOOD MORNING</h1></center>')

def goodafternoon(request):
    return HttpResponse('<center><h1 style=color:pink>GOOD AFTERNOON</h1></center>')

def goodevening(request):
    return HttpResponse('<center><h1 style=color:red>GOOD EVENING</h1></center>')

def goodnight(request):
    return HttpResponse('<center><h1 style=color:brown>GOOD NIGHT</h1></center>')