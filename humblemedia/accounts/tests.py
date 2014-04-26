from django.test import client, TestCase
from django.contrib.auth.models import User


class TestLogin(TestCase):
    def setUp(self):
        self.client = client.Client()
        User.objects.create_user(username='kuncho',
                                 email='kuncho@kunchev.com',
                                 password='secret_kuncho')

    def test_login(self):
        response = self.client.post('/accounts/login/', {
            'username': 'kuncho',
            'password': 'secret_kuncho'
        }, follow=True)
        self.assertTrue(response.context['user'].is_authenticated())
