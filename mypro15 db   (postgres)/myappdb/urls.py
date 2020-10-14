from django.urls import path
from myappdb.views import me
urlpatterns = [
    path('shark/', view=me,name='me'),
]