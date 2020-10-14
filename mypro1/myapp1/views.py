from django.http import HttpResponse
from django.shortcuts import render

# Creating url in project level & defining function based views

def Test(View):
    print("Welcome to Django Class")
    return HttpResponse("<center><h1 style=color:blue;>HELLO WORLD </h1></center>")