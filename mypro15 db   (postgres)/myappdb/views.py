from tokenize import Name

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from myappdb.models import registerinfo


class Me(View):

    def get(self,request,*args,**kargs):
        return render(request,"myreg.html")

    def post(self, request, *args, **kwargs):
        print("something")
        hi= registerinfo()
        hi.Name = request.POST.get('name')
        hi.Age = request.POST.get('age')
        hi.Address = request.POST.get('addrs')
        hi.Phone = request.POST.get('phone')
        hi.Email= request.POST.get('email')
        hi.Zip = request.POST.get('zip')
        hi.save()
        return HttpResponse('<h1>Sucessfully Data entered to Database</h1>')


me=Me.as_view()