from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse
from catalogue.models import Book

#def index(request):
#    return HttpResponse("Hello, world. You're at the catalogue index.")

def index(request):
    books = Book.objects.all()
    return render(request, 'catalogue/index.html', {
        'books': books,
    })

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'catalogue/book_detail.html', {
        'book': book,
    })
