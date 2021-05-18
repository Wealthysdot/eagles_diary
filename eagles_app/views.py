from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Entry


class index(ListView):
    model = Entry
    template_name = "index.html"


class createEntry(CreateView):
    model = Entry
    template_name = "create.html"
    fields = ('entry_title', 'entry_body',)
    success_url = reverse_lazy('index')


class deleteEntry(DeleteView):
    model = Entry
    template_name = "delete.html"
    success_url = reverse_lazy('index')
