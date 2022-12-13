from django.test import SimpleTestCase
from django.urls import resolve, reverse
from yodepApi.views import RegisterAPI

class ApiurlsTests(SimpleTestCase):
    def test_get_users_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterAPI )