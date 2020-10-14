from django.shortcuts import render
from django.views.generic.base import View

# Adding Css and JS to Static Page

class Hi(View):

    def get(self, request, *args, **kwargs):
        print("Sending request is sucessful")
        return render(request, 'index.html')


hi = Hi.as_view()