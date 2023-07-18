from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class LinksDetailView(DetailView):
    pass


class LinkCreateView(CreateView):
    pass


class LinkEditView(UpdateView):
    pass


class LinkDeleteView(DeleteView):
    pass
