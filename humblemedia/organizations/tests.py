from django.test import TestCase, client

from django.contrib.auth.models import User
from .models import Organization


class OrganizationTest(TestCase):
    def setUp(self):
        self.client = client.Client()
        self.user = User.objects.create_user('panda', 'panda@bamboo.cn', 'lovebamboo')
        self.bad_user = User.objects.create_user('redpanda', 'panda@red.bg', 'redhearts')

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

    def test_admin_edit_organization(self):
        self.client.login(username='panda', password='lovebamboo')
        self.client.post('/organizations/add/', {
                         'title': 'Save the pandas',
                         'description': 'I want to save them all',
                         'url': 'www.pandanda.com',
                         'admins': [self.user.pk],
                         'logo': None,
                         })

        organization = Organization.objects.filter(title='Save the pandas')[0]

        response = self.client.post('/organizations/edit/{}/'.format(organization.pk), {
                               'title': 'Save the pandas',
                               'description': 'I want to save them all now',
                               'url': 'www.pandanda.com',
                               'admins': [self.user.pk],
                               'logo': None,
                               },
                               follow=True)

        edit_project = Organization.objects.filter(title='Save the pandas')[0]
        self.assertEqual(edit_project.description, 'I want to save them all now')

    def test_not_admin_edit_organization(self):
        self.client.login(username='redpanda', password='redhearts')
        self.client.post('/organizations/add/', {
                         'title': 'Save the pandas',
                         'description': 'I want to save them all',
                         'url': 'www.pandanda.com',
                         'admins': [self.user.pk],
                         'logo': None,
                         })

        organization = Organization.objects.filter(title='Save the pandas')[0]

        response = self.client.post('/organizations/edit/{}/'.format(organization.pk), {
                               'title': 'Save the pandas',
                               'description': 'I want to save them all now',
                               'url': 'www.pandanda.com',
                               'admins': [self.user.pk],
                               'logo': None,
                               })

        edit_project = Organization.objects.filter(title='Save the pandas')[0]
        self.assertEqual(edit_project.description, 'I want to save them all')

    def test_admin_delete_project(self):
        self.client.login(username='panda', password='lovebamboo')
        self.client.post('/organizations/add/', {
                         'title': 'Save the pandas',
                         'description': 'I want to save them all',
                         'url': 'www.pandanda.com',
                         'admins': [self.user.pk],
                         'logo': None,
                         })

        organization = Organization.objects.filter(title='Save the pandas')[0]
        before_delete = Organization.objects.count()

        response = self.client.post('/organizations/delete/{}/'.format(organization.pk))

        after_delete = Organization.objects.count()

        self.assertEqual(before_delete - 1, after_delete)


