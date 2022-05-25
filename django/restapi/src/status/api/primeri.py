# ovo se radi u shell python manage.py shell (cd u src folder)

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from status.models import Status
from status.api.serializers import StatusSerializer


obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)

qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


'''

Create obj

'''

data = {'user': 1}
serializer = StatusSerializer(data=data) 
serializer.is_valid() # metod provera da li su podaci objekta u redu, tj da li su u formatu JSON (vraca True ili False)
serializer.save() # metod koji cuva objekat, mora da nakon is_valid(

'''

Update obj

'''

obj = Status.objects.first()
data = {'content': 'some new content', 'user':1}
update_serializer = StatusSerializer(obj, data=data) # .errors - metod koji vraca greske, .id - metod koji vraca id objekta
update_serializer.is_valid()
update_serializer.save()

'''

Delete obj

'''

data = {'content': 'please delete me', 'user':1}
create_obj_serializer = StatusSerializer(data=data) 
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

#data = {'user':4}
obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj) 
# create_obj_serializer.is_valid()
# create_obj = create_obj_serializer.save()
print(get_data_serializer.data)

from rest_framework import serializers

class CustomSerializer(serializers.Serializer): # customized serializeri ako neko polje treba da se doda
	content = serializers.CharField()
	email = serializers.EmailField()

data = {'email': 'nemke@gmail.com', 'content':'bla bla, truc truc'}
create_obj_serializer = CustomSerializer(data=data) 
if create_obj_serializer.is_valid():
	valid_data = create_obj_serializer.data
	print(valid_data)