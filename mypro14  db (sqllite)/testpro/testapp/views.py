from django.shortcuts import render
from testapp.models import Studenttb

# Create your views here.
def  Student(request):
    stu_list=Studenttb.objects.all()
    print(stu_list)
    my_dict={'stu_list':stu_list}
    return render(request,'index.html',context=my_dict)

