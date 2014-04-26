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

    def test_login_with_incorrect_credentials(self):
        response = self.client.post('/accounts/login/', {
            'username': 'kuncho',
            'password': 'not_so_secret_kuncho'
        }, follow=True)
        self.assertFalse(response.context['user'].is_authenticated())

    def test_logout(self):
        self.client.login(username='kuncho', password='secret_kuncho')
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated())

    def test_logout_without_being_logged_in(self):
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated())
