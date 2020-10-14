from django.urls import path
from myapp5 import views
urlpatterns = [

    path('one/', views.first_view),
    path('two/', views.second_view),
    path('three/', views.third_view),
    path('four/', views.fourth_view),
]
