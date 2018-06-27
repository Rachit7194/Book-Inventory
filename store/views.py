from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from store.models import Book


class StoreAppFirst(TemplateView):
    template_name = "storedemo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_count'] = Book.objects.all().count()
        return context