from django.urls import path,include
from staticapp.views import info

urlpatterns = [
    path('info/', view=info, name='info'),
]