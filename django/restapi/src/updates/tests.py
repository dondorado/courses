from django.test import TestCase

# # Create your tests here.
# from django.contrib.auth import get_user_model

# User = get_user_model

# class UpdateTestCase(TestCase):
# 	def setUp(self):
# 		user = User.objects.create(username='nemanja', email='nemke@gmail.com')
# 		user.set_password('splituska')
# 		user.save()

# 	def test_created_user(self):
# 		qs = User.objects.filter(username='nemanja')
# 		self.assertEqual(qs.count(), 1)