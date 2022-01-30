from django.test import TestCase
from EDW_Academy.urls import users
from django.urls import resolve


class TestUrls(TestCase):
    def test_url_uses_correct_view(self):
        a = resolve('/usersurl/')
        self.assertEqual(a.func, users)

    def test_view_url_exists(self):
        a = self.client.get('/usersurl/')
        self.assertEqual(a.status_code, 200)



