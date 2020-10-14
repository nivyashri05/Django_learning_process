from django.urls import path
from myapp9.views import hi

urlpatterns = [
    path('page', view=hi, name='hi')
]
