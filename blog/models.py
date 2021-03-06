from django.db import models
from django.core.urlresolvers import reverse


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "entries"


class Comment(models.Model):
    entry = models.ForeignKey(Entry)
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=200)
    body = models.TextField(max_length=1000, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body