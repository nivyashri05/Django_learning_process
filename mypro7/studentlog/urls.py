from django.urls import path, include
from studentlog.views import test
urlpatterns = [
    path('login/', view=test,name='test'),

]