from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

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


class APITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='dummy_two', password='dummy_two12345')
        self.test = Test.objects.create(id=1, name='Test_two', author=self.user)
        self.client = APIClient()
        self.client.login(username=self.user.username, password=self.user.password)
        
    def test_get_questions(self):
        url = '/api/get_questions/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
