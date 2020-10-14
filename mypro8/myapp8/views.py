from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


class Test(View):
    def get(self,request):
        print("something")
        return render(request,'admin.html')


    def post(self,request):
        print("HELLO")
        return HttpResponseRedirect("/one/")

test=Test.as_view()


class Test1(View):
    def get(self, request):
        print("something")
        return render(request, 'login.html')


    def post(self,request):
        print("HELLO")
        return HttpResponseRedirect("/two/")

test1=Test1.as_view()


class Test2(View):
    def get(self,request):
        print("Something")
        return render(request,'register.html')

test2=Test2.as_view()


