from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from django.contrib.auth import get_user_model


User = get_user_model()

class UserAPITestCase(APITestCase):

	def setUp(self):

		user = User.objects.create(username='nemanja', email='nemke@gmail.com')
		user.set_password('splituska')
		user.save()

	def test_created_user_std(self):
		qs = User.objects.filter(username='nemanja')
		self.assertEqual(qs.count(), 1)

	def test_register_user_api_fail(self):
		url = api_reverse('api-auth:register')
		data = {
				'username': 'nemke',
				'email': 'nemke@gmail.com',
				'password': 'splituska'
		}
		response = self.client.post(url, data, format= 'json')
		print(response.status_code)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
