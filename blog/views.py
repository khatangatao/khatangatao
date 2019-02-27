from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .forms import CommentForm
from .models import Entry, Comment


class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')
    paginate_by = 10


class EntryDetail(CreateView):
    model = Entry
    template_name = 'blog/entry_detail.html'
    form_class = CommentForm


    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = super().get_form_kwargs()
        # context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        # kwargs['entry'] = self.object
        kwargs['entry'] = self.get_object()
        return kwargs

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context dict.
        """
        d = super().get_context_data(**kwargs)
        d['entry'] = self.get_object()
        return d

    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        return self.get_object().get_absolute_url()
