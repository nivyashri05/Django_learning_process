from django.shortcuts import render
from django.views.generic.base import View


class Info(View):

    def get(self,request):
        print("something")
        return render(request,'contact.html')

info=Info.as_view()
