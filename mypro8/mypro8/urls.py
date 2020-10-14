
from django.contrib import admin
from django.urls import path
from myapp8 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', views.test),
    path('one/', views.test1),
    path('two/', views.test2),

]
