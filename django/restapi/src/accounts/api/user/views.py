from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, pagination
from .serializers import UserDetailSerializer
from accounts.api.permissions import AnonPermissionOnly
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from status.api.views import StatusAPIView
from rest_framework.response import Response





User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly] u nemanjaapi.restconf.main.py su definisana podesanja pa ovo nema potrebe
	queryset = User.objects.filter(is_active=True) # pojavljuju se samo user koji su aktivni
	serializer_class = UserDetailSerializer
	lookup_field = 'username'

	def get_serializer_context(self):
		return {'request': self.request}





class UserStatusAPIView(StatusAPIView): # - I nacin pretrage
	serializer_class = StatusInlineUserSerializer
	#search_fields = ('user__username', 'content') # ovo zamenjuje queryset, podeseno u main.py serach_param i ordering_param
	# nisu potrebna search fields jer ih vice iz StatusAPIView
	def get_queryset(self, *args, **kwargs):
		username = self.kwargs.get('username', None)
		if username is None:
			return Status.objects.none()
		return Status.objects.filter(user__username=username)

	def post(self, request, *args, **kwargs):
		return Response({'detail': 'Not allowed here'}, status=400)

# class UserStatusAPIView(generics.LISTAPIView): - II nacin pretrage
# 	#queryset = User.objects.filter(is_active=True) # pojavljuju se samo user koji su aktivni
# 	serializer_class = StatusInlineUserSerializer
# 	#pagination_class = NEMANJAAPIPagination # pagination je obelezavanje stranica
# 	#search_fields = ('user__username', 'content') # ovo zamenjuje queryset, podeseno u main.py serach_param i ordering_param
# 	# nisu potrebna search fields jer ih vice iz StatusAPIView
# 	def get_queryset(self, *args, **kwargs):
# 		username = self.kwargs.get('username', None)
# 		if username is None:
# 			return Status.objects.none()
# 		return Status.objects.filter(user__username=username)

# 	def post(self, request, *args, **kwargs):
# 		return Response({'detail': 'Not allowed here'}, status=400)