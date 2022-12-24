from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
from . import forms

# Create your views here.
def book_view(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})


def book_detail_view(request, **kwargs):
    book = Book.objects.get(id=kwargs['id'])
    return render(request, 'book_detail.html', context={'object_detail': book})

def add_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>Книга успешно создана</h1>')
    else:
        form = forms.BookForm()
    return render(request, 'create_book.html', {'form': form})

def update_book_view(request, **kwargs):
    book = get_object_or_404(Book, id=kwargs['id'])
    if request.method == 'POST':
        form = forms.BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Книга успешно обновлена</h1>')
    else:
        form = forms.BookForm(instance=book)
    return render(request, 'book_update.html', {'form': form, 'object': book})


def delete_book_view(request, **kwargs):
    book = get_object_or_404(Book, id=kwargs['id'])
    book.delete()
    return HttpResponse('<h1>Книга удалена</h1>')