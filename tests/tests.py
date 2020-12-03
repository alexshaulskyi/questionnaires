from django.test import TestCase, Client
from rest_framework import status

from users.models import User
from tests.models import Test


class PageCodes(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(username='dummy', password='dummy')
        self.post = Test.objects.create(id=1, name="Test test", author=self.user)
        self.client.post('/auth/login/', {'username': 'dummy', 'password': 'dummy'}, follow=True)

    def test_single_page_registered(self):
        """ Tests if a registered user can access test page """
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, 200)

    def test_new_anonymous_user(self):
        """ Tests if an anonymous user can access test page """
        self.client.logout()
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/?next=/1/')
