from django.shortcuts import render
from django.http import Http404
from catalogue.models import Book
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the catalogue index.")

def index(request):
    count = Book.objects.count()
    return render(request, 'catalogue/index.html', {
        'count': count,
    })

def list(request):
    books = Book.objects.all()
    return render(request, 'catalogue/list.html', {
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

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'type', 'category', 'tags', 'rating', 'description']
    template_name_suffix = '_update'
    #def get_object(self, queryset=None):
    #  object = get_object_or_404(Post,title=self.kwargs['title'])
    #  return object
    success_url = reverse_lazy('list')

class DocListView(ListView):
    model = Book
    #paginate_by = 50

    #def get_queryset(self):
    #    return Book.objects.filter(title__icontains='engineering') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
