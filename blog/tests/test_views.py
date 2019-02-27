from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Entry, Comment
from django_webtest import WebTest


class HomePageTests(TestCase):
    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_two_entries(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')

    def test_no_entries(self):
        response = self.client.get('/')
        self.assertContains(response, 'Пока ничего нет.')

    def test_homepage(self):
        """
        Tests main page
        :return: boolean
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class EntryViewTest(WebTest):
    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.entry = Entry.objects.create(title='1-title', body='1-body', author=self.user)

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)

    def test_no_comments_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, 'Комментариев пока нет.')

    def test_one_comment_in_entry(self):
        self.comment = Comment.objects.create(entry=self.entry, body='comments body', name=self.user)
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, 'comments body')

    def test_view_page(self):
        page = self.app.get(self.entry.get_absolute_url())
        self.assertEqual(len(page.forms), 1)