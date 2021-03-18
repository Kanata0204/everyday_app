from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BookList(TemplateView):
    template_name = 'index.html'

    

# def indexfunc(request):
#     return render(request, 'index.html')