import json

from django.core.serializers import serialize # built-in metod sa serijalizovanje
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from nemanjaapi.mixins import JsonResponseMixin
from .models import Update

# def detail_view(request):
# 	return render() # funkcija vraca Json (JavaScript Object Notation) ili XML data
# 	# return HttpResponse(get_template().render({})) - render modul je skraceni oblik ovoga

def json_example_view(request):
	'''
	GET metod
	'''

	data = {
		'count': 1000,
		"content": "Welcome",
	}

	# json_data = json.dumps(data)
	# return HttpResponse(json_data, content_type='application/json') - ovako se nekad pisao kod pre dolaska JsonResponse (import json iz python)
	return JsonResponse(data)


class JsonCBV(View):
	
	def get(self, request, *args, **kwargs):

		data = {
		'count': 1000,
		"content": "Welcome",
		}

		return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
	
	def get(self, request, *args, **kwargs):
		data = {
		'count': 1000,
		"content": "Welcome",
		}
		return self.render_to_json_response(data)

class SerializedDetailView(View):
	
	def get(self, request, *args, **kwargs):		
		# data = serialize("json", [obj, ], fields= ('user', 'content')) # obj ide kao lista da bi moglo da se iteratuje kroz njega
		# json_data = data
		# data = {
		# 'user': obj.user.username,
		# "content": obj.content, - ako podaci ne trebaju u formi liste
		# }
		# json_data = json.dumps(data)
		obj = Update.objects.get(id=1) # uzimanje objekta sa id 1 klase Update, samo pojedinacni objekti
		json_data = obj.serialize()
		return HttpResponse(json_data, content_type='application/json') # ovako se nekad pisao kod pre dolaska JsonResponse (import json iz python)

class SerializedListView(View):
	
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all() # uzimanje svih objekata klase Update
		# data = serialize("json", qs, fields= ('user', 'content')) # fields je opciono, ako necu sve atribute klase Update
		# json_data = data
		# print(data)
		# data = {
		# 'user': obj.user.username,
		# "content": obj.content,
		# }
		json_data = Update.objects.all().serialize()
		
		return HttpResponse(json_data, content_type='application/json') # ovako se nekad pisao kod pre dolaska JsonResponse (import json iz python)

# python manage.py dumpdata --format json --indent 4 - formula kojom se izbacuju svi podaci za kreirane objekte u vidu fixtures. Ako hocu samo iz odredjene aplikacije stavim npr updates.Update (ide tacka)