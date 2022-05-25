from django.conf import settings
from django.db import models

# Create your models here.

def upload_update_image(instance, filename): # isto kao u updates.model
	return "status/{user}/{filename}".format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
	pass
	


class StatusManager(models.Manager):
	def get_queryset(self):
		return StatusQuerySet(self.model, using=self._db)

class Status(models.Model): # isto kao u updates.model

	user 	  = models.ForeignKey(settings.AUTH_USER_MODEL) 
	content   = models.TextField(blank=True, null=True)	
	image 	  = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = StatusManager()

	def __str__(self):
		return str(self.content)[:50]

	class Meta:
		verbose_name = 'Status post'
		verbose_name_plural = 'Status posts'

	@property
	def owner(self):
		return self.user
	