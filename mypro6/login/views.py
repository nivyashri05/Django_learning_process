from django.shortcuts import render

# Create your views here.

# rendering template with function based views

def Test(request):
    return render(request,'login.html')