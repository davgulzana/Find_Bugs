from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Book
from django.urls import reverse_lazy

class BookList(ListView):
    models = Book


class BookView(DetailView):
    models = Book


class BookCreate(CreateView):
    models = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    models = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    models = Book
    success_url = reverse_lazy('book_list')
