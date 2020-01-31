from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Publication
from .forms import PublicationForm, BookForm

def home_view(request):
    book = get_list_or_404(Book)
    publication = get_list_or_404(Publication, active=True)
    return render(request, 'home.html', {'booklist':book, 'publist':publication})

def add_publication(request):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PublicationForm()
    return render(request, 'form.html', {'form':form,'model_name':'Publication'})

def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, 'form.html', {'form': form, 'model_name':'Book'})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, 'form.html', {'form': form, 'model_name':'Book'})
