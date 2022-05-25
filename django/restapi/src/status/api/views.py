import json

from rest_framework import generics, mixins, permissions # https://www.django-rest-framework.org/api-guide/generic-views/ sajt za django rest_framework
# from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from accounts.api.permissions import IsOwnerOrReadOnly
from status.models import Status
from .serializers import StatusSerializer

# # CreateModelMixin --> handling post data (POST metod)
# # UpdateModelMixin --> handling put data (PUT metod)
# # DestroyModelMixin --> delete data (DELETE metod)

import json


def is_json(json_data):
	try:
		real_json = json.loads(json_data)
		is_valid = True
	except ValueError:
		is_valid = False
	return is_valid		



class StatusAPIDetailView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

	permission_classes 		 = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #- vuce sa nemanjaapi.restconf.main.py default za autentifikaciju, ovde moze override njih
	#authentication_classes	 = []
	serializer_class 		 = StatusSerializer
	queryset = Status.objects.all()
	lookup_field = 'id'

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

	# def perform_update(self, serializer):
	# 	serializer.save(updated_by_user=self.request.user)

	# def perform_destroy(self, instance):
	# 	if instance is not None:
	# 		return instance.delete()
	# 	return None	

class StatusAPIView(mixins.CreateModelMixin,
					generics.ListAPIView):
	permission_classes 		 = [permissions.IsAuthenticatedOrReadOnly] # sa importa, IsAuthenticated ne dozvoljava da nerigistrovani user vidi nesto na stranici dok IsAuthenticatedOrReadOnly moze da vidi, ali ne i da menja sadrzaj, JWT ili OAuth2 su framework bas za to (OAuth2 je third-party, npr povezivanje chess.com sa facebookovim nalogom, dok je JWT vise za autentifikaciju gde nema interakcije sa third-party )
	#authentication_classes	 = [SessionAuthentication] # sa importa
	serializer_class 		 = StatusSerializer
	passed_id 				 = None
	#queryset = Status.objects.all()
	search_fields = ('user__username', 'content', 'user__email') # ovo zamenjuje queryset, podeseno u main.py serach_param i ordering_param
	ordering_fields = ('user__username', 'timestamp') # ovde se podesava koja sve polja mi trebaju za sort
	queryset = Status.objects.all()



	# def get_queryset(self):
	# 	request = self.request
	# 	#print(request.user)
	# 	qs 		= Status.objects.all()
	# 	query   = self.request.GET.get('q') # q je oznaka sta ide posle api/status/?q - ovako ide adresa. Ako nesto hocu da trazim api/status/?q=delete i trazi u content jer je dole zadato tako
	# 	if query is not None:
	# 		qs = qs.filter(content__icontains=query).order_by('timestamp') # minus se stavlja ako hocu kontra
	# 	return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs) # create je built-in metod CreateModelMixin
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
	# def get_object(self):
	# 	request 	= self.request
	# 	passed_id   = request.GET.get('id', None) or self.passed_id
	# 	queryset 	= self.get_queryset()
	# 	obj = None
	# 	if passed_id is not None:
	# 		obj = get_object_or_404(queryset, id=passed_id)
	# 		self.check_object_permissions(request, obj)

	# 	return obj
	

	# def get(self, request, *args, **kwargs):
	# 	url_passed_id   = request.GET.get('id', None)
	# 	json_data = {}
	# 	body_ = request.body
	# 	if is_json(body_):
	# 		json_data = json.loads(request.body)
	# 	new_passed_id = json_data.get('id', None)
	# 	#print(request.body)
	# 	passed_id = url_passed_id or new_passed_id or None
	# 	self.passed_id = passed_id
	# 	if passed_id is not None:
	# 		return self.retrieve(request, *args, **kwargs)

	# 	return super().get(request, *args, **kwargs)

	
	# def put(self, request, *args, **kwargs):
	# 	url_passed_id   = request.GET.get('id', None)
	# 	json_data = {}
	# 	body_ = request.body
	# 	print(request.data) # podaci koji dolaze preko request
	# 	if is_json(body_):
	# 		json_data = json.loads(request.body)
	# 	new_passed_id = json_data.get('id', None)
	# 	#print(request.body)
	# 	passed_id = url_passed_id or new_passed_id or None
	# 	self.passed_id = passed_id
	# 	return self.update(request, *args, **kwargs)

	# def patch(self, request, *args, **kwargs):
	# 	url_passed_id   = request.GET.get('id', None)
	# 	json_data = {}
	# 	body_ = request.body
	# 	if is_json(body_):
	# 		json_data = json.loads(request.body)
	# 	new_passed_id = json_data.get('id', None)
	# 	#print(request.body)
	# 	passed_id = url_passed_id or new_passed_id or None
	# 	self.passed_id = passed_id
	# 	return self.update(request, *args, **kwargs)

	# def delete(self, request, *args, **kwargs):
	# 	url_passed_id   = request.GET.get('id', None)
	# 	json_data = {}
	# 	body_ = request.body
	# 	if is_json(body_):
	# 		json_data = json.loads(request.body)
	# 	new_passed_id = json_data.get('id', None)
	# 	#print(request.body)
	# 	passed_id = url_passed_id or new_passed_id or None
	# 	self.passed_id = passed_id
	# 	return self.destroy(request, *args, **kwargs)

# class StatusListSearchAPIView(APIView):
# 	permission_classes 		= []
# 	authentication_classes  = []

# 	def get(self, request, format=None):
# 		qs 			= Status.objects.all()
# 		serializer  = StatusSerializer(qs, many=True) 
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		qs 			= Status.objects.all()
# 		serializer  = StatusSerializer(qs, many=True) 
# 		return Response(serializer.data)








# 	# def perform_create(self, serializer):
# 	# 	serializer.save(user=self.request.user)

# # class StatusCreateAPIView(generics.CreateAPIView): - nije potrebno jer, StatusApi resava
# # 	permission_classes 		= []
# # 	authentication_classes  = []
# # 	queryset 				= Status.objects.all()
# # 	serializer_class 		= StatusSerializer



# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
# 	permission_classes 		= []
# 	authentication_classes  = []
# 	queryset 				= Status.objects.all()
# 	serializer_class 		= StatusSerializer
# 	#lookup_field = "id" # ovo se stavlja po default, jer u urls gleda po id, ako se ne stavi, moze id u urls da se promeni u pk

# 	# def get_object(self, *args, **kwargs):
# 	# 	kwargs = self.kwargs
# 	# 	kw_id = kwargs.get("id") # II nacin da se ne stavlja lookup_field, get('id') moze u zagradi bilo sta, samo onda mora u urls da se promeni isto to sto je u zagradi
# 	# 	return Status.objects.get(id=kw_id)
# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs) # update je built-in metod UpdateModelMixin

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs) # destroy je built-in metod DestroyModelMixin

# # class StatusUpdateAPIView(generics.UpdateAPIView):
# # 	permission_classes 		= []
# # 	authentication_classes  = []
# # 	queryset 				= Status.objects.all()
# # 	serializer_class 		= StatusSerializer

# # class StatusDeleteAPIView(generics.DestroyAPIView):
# # 	permission_classes 		= []
# # 	authentication_classes  = []
# # 	queryset 				= Status.objects.all()
# # 	serializer_class 		= StatusSerializer

