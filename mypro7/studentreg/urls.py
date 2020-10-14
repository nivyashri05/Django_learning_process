from django.urls import path, include
from studentreg.views import test
urlpatterns = [
    path('register/', view=test,name='test'),

]
