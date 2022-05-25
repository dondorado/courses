from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()

class StatusTestCase(TestCase):
	def setUp(self):
		user = User.objects.create(username='nemanja', email='nemke@gmail.com')
		user.set_password('splituska')
		user.save()

	def test_creating_status(self):
		user = User.objects.get(username='nemanja')
		obj = Status.objects.create(user=user, content='Testiranje')
		self.assertEqual(obj.id, 1)
		qs = Status.objects.all()
		self.assertEqual(qs.count(), 1)