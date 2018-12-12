from django.test import TestCase

from ..models import Entry, Comment

class EntryModelTest(TestCase):
    def test_entry_create(self):
        pass

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")


class CommentModelTest(TestCase):
    def test_string_representation(self):
        comment = Comment(body="My comment body")
        self.assertEqual(str(comment), comment.body)