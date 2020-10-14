from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
# To display date and time
def clock(request):
    x=datetime.datetime.now()
    s='<h1 style="color:blue";> Hello Current Date and Time is :' + str(x) +'</h1>'
    return HttpResponse(s)