from django.contrib import admin

from .forms import StatusForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
	list_display = ['user', '__str__', 'image'] # polja koja se prikazuju na amin stranici, nema potrebe da se ulazi u post ako samo osnovne podatke trazim
	form = StatusForm
	# class Meta:
	# 	model = Status

admin.site.register(Status, StatusAdmin)