from django.test import TestCase
from django.urls import reverse


class UsersListViewTest(TestCase):

    def test_if_view_is_accessible_by_name(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('users'))
        self.assertTemplateUsed(response, 'users.html')


