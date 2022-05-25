import json

from django.views.generic import View
from django.http import HttpResponse
from nemanjaapi.mixins import HttpResponseMixin

from updates.models import Update as UpdateModel # moze i sa ..models
from updates.forms import UpdateModelForm
from .mixins import CSRFExemptMixin


from .utils import is_json

# Creating(Posting), Updating(Putting), Deleting, Retrieving(Getting) --> pojedinacni Update Model

# endpoint je /api/updates/

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
	'''
	Retrieve, Delete, Update  --> pojedinacni objekat

	'''
	is_json = True

	def get_object(self, id=None):
		# try:
		# 	obj = UpdateModel.objects.get(id=id) - validacija da li postoji objekat I nacin
		# except UpdateModel.DoesNotExist:
		# 	obj = None
		# return obj

		qs = UpdateModel.objects.filter(id=id) #validacija da li postoji objekat II nacin
		if qs.count() == 1:
			return qs.first()
		return None
		
			

	def get(self, request, id, *args, **kwargs):

		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({'message': 'Update not found'})
			return self.render_to_response(error_data, status = 404)
		json_data = obj.serialize()
		return self.render_to_response(json_data)

	def post(self, request, *args, **kwargs):
		json_data = json.dumps({'message': 'Not allowed, please use the /api/updates/ endpoint'})
		return self.render_to_response(json_data, status = 403)

	def put(self, request, id, *args, **kwargs):


		#print(dir(request)) # sve mogucnosti koje ima metod request
		#print(request.body) # body je metod za request koji sluzi za put
		#print(request.data)
		
		valid_json = is_json(request.body)

		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON'})
			return self.render_to_response(error_data, status = 400)


		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({'message': 'Update not found'})
			return self.render_to_response(error_data, status = 404)

		data = json.loads(obj.serialize()) # I nacin validacije, obj.serialize je python klasa koja je napravljena u Update model u models.py i koristi se njen metod serialize, zato treba json.loads()
		# saved_data = {
		# 	'user' = obj.user,
		# 	'content' = obj.content itd # II nacin validacije, mora da se napravi recnik koja ima sva polja definisana u klasi Update

		# }
		passed_data = json.loads(request.body)
		#print(passed_data)

		for key, value in passed_data.items():
			data[key] = value
		form = UpdateModelForm(data, instance=obj)

		if form.is_valid():
			obj = form.save(commit=True) # commit je cuvanje izmena (ovaj objekat vuce iz UpdateModelForm-a user, content i image)
			obj_data = json.dumps(data)
			return self.render_to_response(obj_data, status = 201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status = 400)

		json_data = json.dumps({'message': 'Never mind'})	

		return self.render_to_response(json_data)

	def delete(self, request, id, *args, **kwargs):
		obj = self.get_object(id=id)
		if obj is None:
			error_data = json.dumps({'message': 'Object not found'})
			return self.render_to_response(error_data, status = 404)
		deleted_, item_deleted = obj.delete()
		print(deleted_)
		if deleted_ == 1:
			json_data = json.dumps({'message': 'Successfully deleted the object'})	
			return self.render_to_response(json_data, status = 200)
		error_data = json.dumps({'message': 'Object not found'})
		return self.render_to_response(error_data, status = 400) 	


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):

	'''
	List View
	Create View
	Update
	Delete

	'''

	is_json = True
	queryset = None

	def get_queryset(self):
		qs = UpdateModel.objects.all()
		self.queryset = qs
		return qs
	def get_object(self, id=None):
		if id is None:
			return None
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

	def get(self, request, *args, **kwargs):
		data = json.loads(request.body)
		passed_id = data.get("id", None)
		if passed_id is not None:
			obj = self.get_object(id=passed_id)
			if obj is None:
				error_data = json.dumps({'message': 'Object not found'})
				return self.render_to_response(error_data, status = 404)
			json_data = obj.serialize()
			return self.render_to_response(json_data)				
		else:
			qs = self.get_queryset()
			json_data = qs.serialize()
			return self.render_to_response(json_data)

	def post(self, request, *args, **kwargs):
		#print(request.POST)
		valid_json = is_json(request.body)

		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON'})
			return self.render_to_response(error_data, status = 400)		
		data = json.loads(request.body)
		form = UpdateModelForm(data)

		if form.is_valid():
			obj = form.save(commit=True) # commit je cuvanje izmena (ovaj objekat vuce iz UpdateModelForm-a user, content i image)
			obj_data = obj.serialize()
			return self.render_to_response(obj_data, status = 201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status = 400)
		data = {'message': 'Not allowed'}
		return self.render_to_response(data, status = 400) # 400 je bad request

	# def delete(self, request, *args, **kwargs):
	# 	data = json.dumps({'message': 'You cannot delete an entire list'})
	# 	return self.render_to_response(data, status = 403) # 403 je NotAllowed, Forbidden (status je opciono)		

	def put(self, request, *args, **kwargs):
		valid_json = is_json(request.body)

		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON'})
			return self.render_to_response(error_data, status = 400)
		passed_data = json.loads(request.body)
		passed_id = passed_data.get('id', None)
		if not passed_id:
			error_data = json.dumps({'id': 'This is a required field to update item'})
			return self.render_to_response(error_data, status = 400)
		obj = self.get_object(id=passed_id)
		if obj is None:
			error_data = json.dumps({'message': 'Object not found'})
			return self.render_to_response(error_data, status = 404)
		data = json.loads(obj.serialize())
		for key, value in passed_data.items():
			data[key] = value
		form = UpdateModelForm(data, instance=obj)
		if form.is_valid():
			obj = form.save(commit=True)
			obj_data = json.dumps(data)
			return self.render_to_response(obj_data, status = 201)
		if form.errors:
			data = json.dumps(form.errors)
			return self.render_to_response(data, status = 400)
		json_data = json.dumps({'message': 'Never mind'})
		return self.render_to_response(json_data)

	def delete(self, request, *args, **kwargs):
		valid_json = is_json(request.body)

		if not valid_json:
			error_data = json.dumps({'message': 'Invalid data sent, please send using JSON'})
			return self.render_to_response(error_data, status = 400)


		passed_data = json.loads(request.body)
		passed_id = passed_data.get('id', None)

		if not passed_id:
			error_data = json.dumps({'id': 'This is a required field to update item'})
			return self.render_to_response(error_data, status = 400)

		obj = self.get_object(id=passed_id)
		if obj is None:
			error_data = json.dumps({'message': 'Object not found'})
			return self.render_to_response(error_data, status = 404)
		deleted_, item_deleted = obj.delete()
		print(deleted_)
		if deleted_ == 1:
			json_data = json.dumps({'message': 'Successfully deleted the object'})	
			return self.render_to_response(json_data, status = 200)
		error_data = json.dumps({'message': 'Object not found'})
		return self.render_to_response(error_data, status = 400) 	
	