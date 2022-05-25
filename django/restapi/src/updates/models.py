import json
from django.conf import settings
from django.db import models
from django.core.serializers import serialize

def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename=filename)



class UpdateQuerySet(models.QuerySet): # za list view json
	# def serialize(self): # I nacin
	# 	qs = self
	# 	return serialize("json", qs, fields=('user', 'content', 'image'))

	# def serialize(self): # II nacin
	# 	qs = self
	# 	final_list = []
	# 	for obj in qs:
	# 		final_list.append(obj.serialize())
	# 	return final_list

	# def serialize(self): # III nacin
	# 	qs = self
	# 	final_list = []
	# 	for obj in qs:
	# 		stuct = json.loads(obj.serialize())
	# 		final_list.append(stuct)
	# 	return json.dumps(final_list) # bez json.dumps je samo obican set, ovako je upakovan u listu

	def serialize(self): # IV nacin
		list_values = list(self.values('user', 'content', 'image', 'id')) # uzimanje iz recnik sta treba od vrednosti sa metodom values
		print(list_values)
		
		return json.dumps(list_values)


class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
	user 	  = models.ForeignKey(settings.AUTH_USER_MODEL)
	content   = models.TextField(blank=True, null=True)	
	image 	  = models.ImageField(upload_to=upload_update_image, blank=True, null=True) # za koriscenje ImageField mora da se instalira Pillow (pip install pillow)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True) #svaki put kad je objekat kreiran stavi vreme na trenutno (tj momenat kad je kreiran). Iako se objekat kasnije mozda promeni, ostavlja vreme prvobitnog kreiranja. Opcija auto_now daje mogucnost azuriranja vremena kreiranja

	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	# def serialize(self): # za detail view json I nacin
	# 	json_data = serialize("json", [self], fields=('user', 'content', 'image'))
	# 	stuct = json.loads(json_data) # obrnuto od json.dumps(), vraca recnik upakovan u listu
	# 	print(stuct)
	# 	data = json.dumps(stuct[0]['fields']) # obzirom da vraca listu, 0 je prvi element liste (recnik), a fields je kljuc. Fakticki vraca vrednosti fields kljuca
	# 	return data

	def serialize(self): # za detail view json II nacin
		try:
			image = self.image.url # ako self.image nije None u gore iznad redu, vraca url slike
		except:
			image = ""
		data = {
		'id': self.id,
		'content': self.content,
		"user": self.user.id, # id je atribut user
		'image': image
		}
		data = json.dumps(data)
		return data
		