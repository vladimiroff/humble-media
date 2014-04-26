import os

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase, client

from .models import Resource


class ResourceTest(TestCase):
    def setUp(self):
        self.client = client.Client()
        self.user = User.objects.create_user('panda', 'panda@bamboo.cn', 'lovebamboo')
        self.bad_user = User.objects.create_user('redpanda', 'panda@red.bg', 'redhearts')
        self.valid_record = {
            'title': 'Save the pandas',
            'description': 'I want to save them all',
            'author': self.user,
            'min_price': 50,
            'is_published': True,
        }

    def test_logged_user_add_resource(self):
        self.client.login(username='panda', password='lovebamboo')
        before_add = Resource.objects.count()
        response = self.client.post('/resources/add/', self.valid_record)
        after_add = Resource.objects.count()
        self.assertEqual(before_add + 1, after_add)

    def test_not_logged_user_add_resource(self):
        before_add = Resource.objects.count()
        response = self.client.post('/resources/add/', self.valid_record)
        after_add = Resource.objects.count()
        self.assertEqual(before_add, after_add)

    def test_admin_edit_resource(self):
        self.client.login(username='panda', password='lovebamboo')
        self.client.post('/resources/add/', self.valid_record)

        resource = Resource.objects.filter(title='Save the pandas')[0]

        self.valid_record['description'] += " now"
        response = self.client.post(
            '/resources/{}/edit/'.format(resource.pk),
            self.valid_record, follow=True)

        edit_project = Resource.objects.filter(title='Save the pandas')[0]
        self.assertEqual(edit_project.description, 'I want to save them all now')

    def test_not_admin_edit_resource(self):
        self.client.login(username='redpanda', password='redhearts')
        self.client.post('/resources/add/', self.valid_record)

        resource = Resource.objects.filter(title='Save the pandas')[0]

        response = self.client.post('/resources/{}/edit/'.format(resource.pk), self.valid_record)

        edit_project = Resource.objects.filter(title='Save the pandas')[0]
        self.assertEqual(edit_project.description, 'I want to save them all')

    def test_admin_delete_resource(self):
        self.client.login(username='panda', password='lovebamboo')
        self.client.post('/resources/add/', self.valid_record)

        resource = Resource.objects.filter(title='Save the pandas')[0]
        before_delete = Resource.objects.count()

        response = self.client.post('/resources/{}/delete/'.format(resource.pk))

        after_delete = Resource.objects.count()

        self.assertEqual(before_delete - 1, after_delete)
