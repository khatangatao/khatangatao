from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import CommentForm
from .models import Entry


class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')
    paginate_by = 10


class AuthorList(ListView):
    template_name = 'authors.html'
    queryset = User.objects.order_by('pk')
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


#  временное место для API View
from .serializers import EntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from blog.api.auth.bearer import BearerTokenAuthentication


class EntryApi(ModelViewSet):
    """Convert data to JSON format and vice versa"""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (BearerTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
    )
