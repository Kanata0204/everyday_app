from django.urls import path, include
from .views import indexfunc

urlpatterns = [
    path('', indexfunc, name='index'),
]
