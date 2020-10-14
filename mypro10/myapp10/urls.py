from django.urls import path,include
from myapp10.views import test
urlpatterns = [

    path('info/', view=test, name='test'),
]

