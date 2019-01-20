from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Entry, Comment

class EntryModelTest(TestCase):
    def test_entry_create(self):
        pass

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

    def test_get_absolute_url(self):
        user = get_user_model().objects.create(username='some_user')
        entry = Entry.objects.create(title="My entry title", author=user)
        self.assertIsNotNone(entry.get_absolute_url())




class CommentModelTest(TestCase):
    def test_string_representation(self):
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), comment.body)