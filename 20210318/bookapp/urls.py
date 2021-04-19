from django.urls import path
from .views import BookList, BookSortingView
# from .views import sortfunc

urlpatterns = [
    path('', BookList.as_view(), name='book'),
    path("book/sorting/", BookSortingView.as_view(), name='book-sorting'),
    # path('sorted/', sortfunc, name='book-sorted')
]
