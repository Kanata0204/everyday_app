from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book

import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

import json

# Create your views here.
class BookList(TemplateView):
    template_name = 'index.html'

    
class BookSortingView(ListView):
    template_name = 'list.html'
    model = Book

    def post(self, request):
        card_text = json.loads(request.POST.get('text'))

        print(card_text, type(card_text))

        for card in card_text:
            book = get_object_or_404(Book, pk=int(card['pk']))
            book.position = card['order']
            book.save()
            
            print(card['pk'], card['order'])
            print('------------------')

        result = f"I'v got: {card_text}"
        return JsonResponse({'data': result}, status=200)

# @csrf_exempt
# def sortfunc(request):
#     books = json.loads(request.POST.get('sort'))
#     for b in books:
#         book = get_object_or_404(Book, pk=int(b['pk']))
#         book.position = b['order']
#         book.save()
#     return HttpResponse('saved')

# def indexfunc(request):
#     return render(request, 'index.html')