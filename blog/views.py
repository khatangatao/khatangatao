from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Entry


class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')
