from .views import indexfunc

from django.urls import path

urlpatterns = [
    path('', indexfunc)
]
