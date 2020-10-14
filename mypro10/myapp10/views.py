from django.shortcuts import render
from django.views.generic.base import View


class Test(View):
    def get(self,request):
        print("something")
        return render(request,'index.html')

test=Test.as_view()

