from django.shortcuts import render
from django.views.generic.base import View

# class based view (with rending templates)


class Test(View):
    def get(self,request):
        x='admin.html'
        return render(request,x)
test=Test.as_view()
