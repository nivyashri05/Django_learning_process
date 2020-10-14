from django.urls import path, include
from adminlog.views import test
urlpatterns = [
    path('adlogin/', view=test,name='test'),

]
