from django.test import TestCase, client

from django.contrib.auth.models import User
from .models import Organization


class OrganizationTest(TestCase):
    def setUp(self):
        self.client = client.Client()
        self.user = User.objects.create_user('panda', 'panda@bamboo.cn', 'lovebamboo')

    def test_logged_user_add_organization(self):
        self.client.login(username='panda', password='lovebamboo')
        before_add = Organization.objects.count()
        response = self.client.post('/organizations/add/', {
                               'title': 'Save the pandas',
                               'description': 'I want to save them all',
                               'url': 'www.pandanda.com',
                               'admins': [self.user.pk],
                               'logo': None,
                               })
        after_add = Organization.objects.count()
        self.assertEqual(before_add + 1, after_add)

    def test_not_logged_user_add_organization(self):
        before_add = Organization.objects.count()
        response = self.client.post('/organizations/add/', {
                               'title': 'Save the pandas',
                               'description': 'I want to save them all',
                               'url': 'www.pandanda.com',
                               'admins': [self.user.pk],
                               'logo': None,
                               })
        after_add = Organization.objects.count()
        self.assertEqual(before_add, after_add)
